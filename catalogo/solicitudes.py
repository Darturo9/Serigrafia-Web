"""Validación y mensajes WhatsApp; no crea clientes ni pedidos."""
from datetime import date
from urllib.parse import urlencode
from django import forms
from .models import Producto

WHATSAPP_NUMERO = "50247233834"  # PDF + código confirmado directamente por el usuario.


def enlace_whatsapp(mensaje):
    return f"https://wa.me/{WHATSAPP_NUMERO}?" + urlencode({"text": mensaje})


class CotizacionForm(forms.Form):
    cantidad = forms.IntegerField(label="Cantidad total", min_value=1)
    def __init__(self, producto_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.producto = Producto.objects.filter(
            pk=producto_id, publicado=True, es_ejemplo=False,
        ).first()
        if self.producto:
            if self.producto.tallas == ['Todas las tallas']:
                self.fields['tallas_solicitadas'] = forms.CharField(
                    label='Tallas que necesitas (opcional)', max_length=200, required=False,
                    help_text='Por ejemplo: 2 M y 1 L. Confirma las medidas con JYZ por WhatsApp.',
                )
                return
            for index, talla in enumerate(self.producto.tallas):
                self.fields[f"talla_{index}"] = forms.IntegerField(
                    label=f"Cantidad en talla {talla}", min_value=0,
                    required=False, initial=0,
                )

    def clean(self):
        datos = super().clean()
        # Volver a consultar: un producto puede ocultarse o cambiar sus opciones
        # después de construir el formulario y antes de validarlo.
        actual = None
        if self.producto:
            actual = Producto.objects.filter(
                pk=self.producto.pk, publicado=True, es_ejemplo=False,
            ).first()
        if not actual or actual.tallas != self.producto.tallas:
            raise forms.ValidationError(
                "El producto o sus opciones cambiaron. Revisa el catálogo antes de continuar."
            )
        self.producto = actual
        if actual.tallas == ['Todas las tallas']:
            datos['distribucion'] = {}
            return datos
        distribucion = {
            talla: datos.get(f"talla_{index}") or 0
            for index, talla in enumerate(actual.tallas)
        }
        if actual.tallas and not self.errors and sum(distribucion.values()) != datos.get("cantidad"):
            raise forms.ValidationError(
                "La suma de las cantidades por talla debe coincidir con la cantidad total."
            )
        datos["distribucion"] = distribucion
        return datos

    def mensaje(self):
        if not self.is_valid():
            raise ValueError("La solicitud debe ser válida antes de preparar el mensaje.")
        datos = self.cleaned_data
        lineas = ["Hola JYZ, quisiera solicitar una cotización.",
                  f"Producto: {self.producto.nombre}",
                  f"Cantidad total: {datos['cantidad']}"]
        if self.producto.tallas == ['Todas las tallas']:
            lineas.append('Tallas solicitadas: ' + (datos.get('tallas_solicitadas') or 'las confirmaré en el chat.'))
        elif datos["distribucion"]:
            lineas.append("Cantidades por talla:")
            lineas.extend(f"- {talla}: {cantidad}" for talla, cantidad in datos["distribucion"].items() if cantidad)
        else:
            lineas.append("Tallas/opciones: necesito consultarlas.")
        lineas.extend(["Adjuntaré mi diseño directamente en este chat.",
                       "Por favor, confirmen disponibilidad, precio y entrega."])
        return "\n".join(lineas)

    def url_whatsapp(self):
        return enlace_whatsapp(self.mensaje())


class IdeaForm(forms.Form):
    """Idea libre del cliente; solo prepara texto para WhatsApp."""
    nombre = forms.CharField(label="Tu nombre (opcional)", max_length=80, required=False)
    prenda = forms.CharField(
        label="¿Qué quieres personalizar? (opcional)", max_length=80, required=False,
        widget=forms.TextInput(attrs={"placeholder": "Camisetas, hoodies, gorras…"}),
    )
    cantidad = forms.IntegerField(label="Cantidad aproximada (opcional)", min_value=1, required=False)
    fecha = forms.DateField(
        label="¿Para cuándo lo necesitas? (opcional)", required=False,
        widget=forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
    )
    idea = forms.CharField(
        label="Cuéntanos tu idea", max_length=1000,
        widget=forms.Textarea(attrs={"rows": 5, "placeholder": "Colores, estilo, dónde va el diseño, para qué ocasión…"}),
        help_text="Tu diseño o imágenes de referencia los adjuntas después en WhatsApp.",
    )

    def clean_nombre(self):
        return " ".join(self.cleaned_data["nombre"].split())

    def clean_prenda(self):
        return " ".join(self.cleaned_data["prenda"].split())

    def clean_fecha(self):
        fecha = self.cleaned_data["fecha"]
        if fecha and fecha < date.today():
            raise forms.ValidationError("Elige una fecha a partir de hoy.")
        return fecha

    def clean_idea(self):
        idea = self.cleaned_data["idea"].strip()
        if not idea:
            raise forms.ValidationError("Escribe tu idea.")
        return idea

    def mensaje(self):
        if not self.is_valid():
            raise ValueError("La idea debe ser válida antes de preparar el mensaje.")
        datos = self.cleaned_data
        saludo = f"Hola JYZ, soy {datos['nombre']}." if datos["nombre"] else "Hola JYZ."
        lineas = [saludo, "Quisiera cotizar una idea para personalizar.", ""]
        if datos["prenda"]:
            lineas.append(f"*Producto:* {datos['prenda']}")
        if datos["cantidad"]:
            lineas.append(f"*Cantidad aproximada:* {datos['cantidad']}")
        if datos["fecha"]:
            lineas.append(f"*Para el:* {datos['fecha']:%d/%m/%Y}")
        lineas.extend(["*Mi idea:*", datos["idea"], "",
                       "Adjuntaré mi diseño o referencias en este chat.",
                       "¿Me confirman opciones, precio y tiempo de entrega?"])
        return "\n".join(lineas)

    def url_whatsapp(self):
        return enlace_whatsapp(self.mensaje())


class SeguimientoForm(forms.Form):
    referencia = forms.CharField(label="Referencia del pedido", max_length=80, required=False)

    def clean_referencia(self):
        referencia = self.cleaned_data["referencia"]
        if any(ord(char) < 32 for char in referencia):
            raise forms.ValidationError("Escribe la referencia en una sola línea.")
        return referencia

    def mensaje(self):
        if not self.is_valid():
            raise ValueError("La consulta debe ser válida antes de preparar el mensaje.")
        referencia = self.cleaned_data["referencia"]
        return (f"Hola JYZ, quisiera consultar el avance de mi pedido. Referencia: {referencia}."
                if referencia else "Hola JYZ, quisiera consultar el avance de mi pedido. No tengo una referencia a mano.")

    def url_whatsapp(self):
        return enlace_whatsapp(self.mensaje())

# ADR 001. Stack y alojamiento

## Estado

**Reemplazado parcialmente por ADR 004 el 8 de octubre de 2026:** Railway sustituye la elección Workers/Hyperdrive. Se conservan Django, Admin y Supabase. El contenido siguiente registra la propuesta original y su prueba; no acredita un alojamiento aceptado ni autoriza compras o configuración externa.

## Contexto

La página quedará al emprendimiento, que necesita mantener productos y fotos. Los pedidos se atienden por WhatsApp. El usuario prefiere Django y solicita dominio y alojamiento en Cloudflare con PostgreSQL gratuito en Supabase.

## Decisión

Evaluar Django con plantillas, Bootstrap y JavaScript, Django Admin, Workers con Python, Hyperdrive/psycopg, PostgreSQL de Supabase Free y Supabase Storage. Comprar el dominio en Cloudflare Registrar solo cuando exista autorización y nombre confirmado.

## Razones

Django Admin evita desarrollar un panel personalizado para un catálogo sencillo. Una sola aplicación mantiene web y administración. PostgreSQL guarda datos y Storage conserva fotos. Los enlaces de WhatsApp permiten atención manual sin construir pedidos o pagos dentro del sitio.

## Consecuencias

Workers requiere validar compatibilidad completa de Django, ORM, sesiones e imágenes. Supabase Free tiene límites operativos. El dominio y posibles planes de alojamiento requieren presupuesto. Una guía y responsables son necesarios para entregar una web mantenible.

## Condición para confirmar

Completar la prueba definida en la especificación de arquitectura y registrar evidencia. Si falla, no cambiar proveedor o base de datos silenciosamente: presentar el hallazgo y documentar una decisión reemplazante acordada con el usuario.

## Alternativas discutidas

WordPress, Astro con un gestor de contenido, Next.js con un gestor de contenido y alojamiento convencional para Django. No son parte del stack actual. Vercel se descartó como destino tras la aclaración del usuario.

## Referencias

`docs/specs/04-arquitectura-y-datos.md` contiene las fuentes técnicas y el flujo propuesto. La presentación de cinco diapositivas comunica el alcance funcional sin detalles tecnológicos.

## Resultado parcial del 8 de octubre

Workers Free probado en cuenta real con CA/Hyperdrive y primera versión protegida. Django falla por límite de CPU en peticiones autorizadas. Esta decisión continúa **propuesta, sin confirmar**; no se cambió proveedor ni plan. Evaluación Paid o alternativa requiere acuerdo del usuario. Ver ../plan/evidencia-cloudflare-prueba.md.

-- PROPUESTA: ejecutar solo tras autorización, después de catalogo.0004.
-- Únicamente tabla nueva; esquema privado del proyecto kcahxuvfmrzxzlnpezyf.
ALTER TABLE jyz_prueba.catalogo_galeriaimagen ENABLE ROW LEVEL SECURITY;
CREATE POLICY jyz_app_servidor ON jyz_prueba.catalogo_galeriaimagen
    TO jyz_app USING (true) WITH CHECK (true);
REVOKE DELETE ON jyz_prueba.catalogo_galeriaimagen FROM jyz_app;
-- Permisos Django: preparar_rol_catalogo añade ver/agregar/cambiar galería,
-- conserva permisos de productos y fotos y no concede borrado ni usuarios.

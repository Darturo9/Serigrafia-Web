-- APLICADO EN PRUEBA EL 8 DE OCTUBRE DE 2026 (con corrección de permisos separada). Solo proyecto kcahxuvfmrzxzlnpezyf.
-- Requiere autorización expresa y comprobar que jyz_prueba no está expuesto a Data API.
-- No contiene contraseñas; activar LOGIN y provisionar secretos por canal seguro por separado.
BEGIN;
CREATE ROLE jyz_migrator NOLOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT NOBYPASSRLS;
CREATE ROLE jyz_app NOLOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT NOBYPASSRLS;
-- Membresía temporal necesaria porque postgres no es superusuario en Supabase.
GRANT jyz_migrator TO postgres WITH INHERIT FALSE, SET TRUE;
CREATE SCHEMA jyz_prueba AUTHORIZATION jyz_migrator;
REVOKE ALL ON SCHEMA jyz_prueba FROM PUBLIC, anon, authenticated;
GRANT CONNECT ON DATABASE postgres TO jyz_migrator, jyz_app;
-- GRANT USAGE debe ejecutarse como propietario; se aplica abajo.
ALTER ROLE jyz_migrator IN DATABASE postgres SET search_path TO jyz_prueba;
ALTER ROLE jyz_app IN DATABASE postgres SET search_path TO jyz_prueba;
SET LOCAL ROLE jyz_migrator;
GRANT USAGE ON SCHEMA jyz_prueba TO jyz_app;
ALTER DEFAULT PRIVILEGES FOR ROLE jyz_migrator IN SCHEMA jyz_prueba GRANT ALL ON TABLES TO jyz_migrator;
ALTER DEFAULT PRIVILEGES FOR ROLE jyz_migrator IN SCHEMA jyz_prueba GRANT ALL ON SEQUENCES TO jyz_migrator;
ALTER DEFAULT PRIVILEGES FOR ROLE jyz_migrator IN SCHEMA jyz_prueba
    REVOKE ALL ON TABLES FROM PUBLIC, anon, authenticated;
ALTER DEFAULT PRIVILEGES FOR ROLE jyz_migrator IN SCHEMA jyz_prueba
    GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO jyz_app;
ALTER DEFAULT PRIVILEGES FOR ROLE jyz_migrator IN SCHEMA jyz_prueba
    GRANT USAGE, SELECT ON SEQUENCES TO jyz_app;
RESET ROLE;
REVOKE jyz_migrator FROM postgres;
COMMIT;
-- Las migraciones se ejecutan posteriormente como jyz_migrator, fuera del Worker.
-- Sin membresía persistente de postgres; sin cambios a auth, storage o realtime.

# Inspección de Supabase mediante MCP

Fecha: 7 de octubre de 2026, Guatemala. Estado: lectura remota verificada; integración Django/Storage/Workers pendiente.

## Autorización y conexión

El usuario autorizó inspección remota de solo lectura y preparación local. No autorizó migraciones, configuración externa, publicación, compras, instalación, commit ni push.

Se usaron herramientas del servidor autenticado `mcp__supabase__*`, sin parámetro de proyecto porque el servidor está limitado a la referencia configurada. `get_project_url({})` devolvió `https://kcahxuvfmrzxzlnpezyf.supabase.co`, que coincide con la referencia proporcionada. Después se ejecutaron consultas SELECT de metadatos y conteos.

Esta evidencia confirma acceso de lectura al proyecto correcto. No acredita permisos de escritura, conexión directa desde Django, Storage HTTP ni Cloudflare. El conector `mcp__codex_apps__supabase_*` falló en la sesión anterior y no se volvió a utilizar; su estado actual no fue comprobado.

## Resultados

- Base: `postgres`; versión informada por el servidor: PostgreSQL **17.11**.
- Esquemas: `auth`, `extensions`, `graphql`, `graphql_public`, `information_schema`, `pg_catalog`, `pg_toast`, `pgbouncer`, `public`, `realtime`, `storage`, `vault`.
- `public`: ninguna tabla ni vista en el inventario de relaciones consultado.
- No aparece `catalogo_producto`, ninguna tabla Django ni un esquema propio de JYZ.
- `storage.buckets`: **0**; `storage.objects`: **0**, por conteos exactos.
- `list_migrations({})`: lista vacía. Esto se refiere al historial consultado por el MCP; los servicios internos sí tienen tablas de migraciones.

| Esquema no perteneciente al catálogo del sistema | Tablas, incluidas particionadas | Vistas |
|---|---:|---:|
| auth | 27 | 0 |
| extensions | 0 | 2 |
| graphql | 0 | 0 |
| graphql_public | 0 | 0 |
| pgbouncer | 0 | 0 |
| public | 0 | 0 |
| realtime | 3 | 0 |
| storage | 8 | 0 |
| vault | 1 | 1 |

Inventario de tablas encontrado:

- `auth`: audit_log_entries, custom_oauth_providers, flow_state, identities, instances, mfa_amr_claims, mfa_challenges, mfa_factors, mfa_recovery_code_sets, mfa_recovery_codes, oauth_authorizations, oauth_client_states, oauth_clients, oauth_consents, one_time_tokens, refresh_tokens, saml_providers, saml_relay_states, schema_migrations, scim_tokens, scim_users, sessions, sso_domains, sso_providers, users, webauthn_challenges, webauthn_credentials.
- `realtime`: messages (particionada), schema_migrations, subscription.
- `storage`: buckets, buckets_analytics, buckets_vectors, migrations, objects, s3_multipart_uploads, s3_multipart_uploads_parts, vector_indexes.
- `vault`: secrets. Su contenido y la vista decrypted_secrets **no se consultaron**.
- Vistas: `extensions.pg_stat_statements`, `extensions.pg_stat_statements_info`, `vault.decrypted_secrets`. Solo se registraron nombres.

`list_tables` confirmó RLS en buckets y objects. Hay tablas internas con RLS desactivado; este inventario no constituye una auditoría de exposición, grants o seguridad. No cambiar tablas administradas por Supabase. No se leyeron filas de usuarios, sesiones, tokens, secretos, logs ni estadísticas SQL.

## Consultas reproducibles de solo lectura

Herramientas usadas: `get_project_url`, `list_tables` (esquemas no pertenecientes al catálogo del sistema, `verbose=false`), `execute_sql` y `list_migrations`.

```sql
SELECT nspname AS schema_name
FROM pg_catalog.pg_namespace ORDER BY nspname;

SELECT n.nspname AS schema_name, c.relname AS relation_name,
       c.relkind, c.relrowsecurity AS rls_enabled
FROM pg_catalog.pg_class c
JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname NOT IN ('pg_catalog', 'information_schema', 'pg_toast')
  AND c.relkind IN ('r', 'p', 'v', 'm', 'f')
ORDER BY 1, 2;

SELECT n.nspname AS schema_name,
       count(*) FILTER (WHERE c.relkind IN ('r','p')) AS tables,
       count(*) FILTER (WHERE c.relkind IN ('v','m')) AS views
FROM pg_catalog.pg_namespace n
LEFT JOIN pg_catalog.pg_class c
  ON c.relnamespace = n.oid AND c.relkind IN ('r','p','v','m','f')
WHERE n.nspname NOT IN ('pg_catalog','information_schema','pg_toast')
GROUP BY n.nspname ORDER BY n.nspname;

SELECT id, name, public, file_size_limit, allowed_mime_types
FROM storage.buckets ORDER BY id;

SELECT current_database() AS database_name,
       current_setting('server_version') AS server_version,
       (SELECT count(*) FROM storage.buckets) AS bucket_count,
       (SELECT count(*) FROM storage.objects) AS object_count;
```

No se ejecutaron DDL/DML, migraciones, creación de buckets, cargas de archivos ni despliegues. Los resultados se resumieron sin credenciales. Próximo paso: [plan de viabilidad](prueba-alojamiento.md).

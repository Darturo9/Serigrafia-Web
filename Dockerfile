FROM python:3.11.16-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.railway.txt /app/
RUN pip install --no-cache-dir --require-hashes -r requirements.railway.txt
COPY manage.py /app/
COPY config /app/config
COPY catalogo /app/catalogo
COPY ops/supabase-root-2021.crt /app/ops/supabase-root-2021.crt
COPY scripts/railway_start.py /app/scripts/railway_start.py
RUN DJANGO_SETTINGS_MODULE=config.settings_static_build python manage.py collectstatic --noinput \
    && useradd --create-home --uid 10001 jyz
USER jyz
ENV DJANGO_SETTINGS_MODULE=config.settings_railway PGSSLROOTCERT=/app/ops/supabase-root-2021.crt
CMD ["python", "scripts/railway_start.py"]

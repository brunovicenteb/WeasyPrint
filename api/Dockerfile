FROM python:3.11-slim

# Instala libs nativas do WeasyPrint
RUN apt-get update && apt-get install -y \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libpangoft2-1.0-0 \
    libharfbuzz0b \
    libfreetype6 \
    libjpeg-dev \
    libxml2 \
    libxslt1.1 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    libssl-dev \
    libcairo2 \
    fontconfig \
    && rm -rf /var/lib/apt/lists/*

# Copia o repositório todo (api + lib)
WORKDIR /app
COPY .. .

# Instala o fork local
RUN pip install .

# Instala dependências da API
WORKDIR /app/api
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]
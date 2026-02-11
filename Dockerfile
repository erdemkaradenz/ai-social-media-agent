# 1. Python'un hafif sürümünü baz al
FROM python:3.10-slim

# 2. Çalışma klasörünü ayarla
WORKDIR /app

# 3. Gereksinimleri kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Tüm kodları kopyala
COPY . .

# 5. Portu dışarı aç (FastAPI varsayılan portu)
EXPOSE 8000

# 6. Uygulamayı başlat
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
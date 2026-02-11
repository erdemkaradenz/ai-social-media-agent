# 1. Node.js'in hafif sürümünü baz al
FROM node:22-alpine

# 2. Çalışma klasörü
WORKDIR /app

# 3. Paket listesini kopyala ve yükle
COPY package.json package-lock.json ./
RUN npm install

# 4. Kodları kopyala
COPY . .

# 5. Vite portunu aç
EXPOSE 5173

# 6. Başlat (--host parametresi önemli)
CMD ["npm", "run", "dev", "--", "--host"]
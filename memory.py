import json
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
import os


def create_memory_index(file_path="examples.json"):
    """JSON dosyasındaki örnekleri okur ve FAISS vektör veritabanına çevirir."""
    print("🧠 Hafıza (Memory) oluşturuluyor...")
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"⚠️ Uyarı: {file_path} bulunamadı. Boş hafıza oluşturuluyor.")
        data = []
    
    texts = [item["content"] for item in data]
    metadatas = [{"platform": item["platform"]} for item in data]
    
    ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://host.docker.internal:11434")
    
    print(f"🔗 Ollama Bağlantı Adresi: {ollama_base_url}")

    embeddings = OllamaEmbeddings(
        model="llama3", 
        base_url=ollama_base_url
    )
    
    if texts:
        vector_store = FAISS.from_texts(texts, embeddings, metadatas=metadatas)
    else:
        
        vector_store = FAISS.from_texts(["Başlangıç verisi"], embeddings, metadatas=[{"platform": "test"}])

    print("✅ Hafıza hazır! Vektörler oluşturuldu.")
    return vector_store

def retrieve_similar_styles(vector_store, query_text, k=2):
    """Gelen yeni konuya (query) en çok benzeyen k adet eski postu bulur."""
    docs = vector_store.similarity_search(query_text, k=k)
    return [doc.page_content for doc in docs]

if __name__ == "__main__":
    if os.path.exists("examples.json"):
        db = create_memory_index()
        
        soru = "Yazılım öğrenmek zor mu?"
        print(f"\n🔍 Soru: {soru}")
        print("Benzer Geçmiş Postlar Aranıyor...")
        
        benzerler = retrieve_similar_styles(db, soru)
        
        for i, post in enumerate(benzerler):
            print(f"{i+1}. Bulunan Örnek: {post}")
    else:
        print("❌ 'examples.json' bulunamadı, test yapılamıyor.")
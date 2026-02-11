import requests
import json
import os

def generate_text_ollama(prompt, model="llama3", temperature=0.7):
    base_url = os.getenv("OLLAMA_BASE_URL", "http://host.docker.internal:11434")
    api_url = f"{base_url}/api/generate"

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "temperature": temperature
    }

    try:
        response = requests.post(api_url, json=payload, timeout=60)
        return response.json()['response']
    except requests.exceptions.ConnectionError:
        return "❌ Hata: Ollama'ya bağlanılamadı. Ollama açık mı?"

if __name__ == "__main__":
    print("⏳ AI Düşünüyor (Ollama)...")
    
    cevap = generate_text_ollama("Bana yazılımcı olmakla ilgili tek cümlelik komik bir söz söyle.")
    
    print("\n🤖 AI Cevabı:")
    print(cevap)
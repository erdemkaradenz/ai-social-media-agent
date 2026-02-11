from agent import ContentAgent
from memory import create_memory_index

vector_store = create_memory_index() 
agent = ContentAgent(vector_store)

print("\n--------------------------------")
print("🤖 AI SOCIAL MEDIA AGENT HAZIR")
print("--------------------------------\n")

secim = input("Giriş türü nedir? (1: Konu, 2: URL): ")

if secim == "1":
    input_data = input("Konuyu yazın: ")
    input_type = "topic"
else:
    input_data = input("URL yapıştırın: ")
    input_type = "url"

platform = input("Hangi platform? (linkedin/twitter): ")

sonuc = agent.run(input_data, platform, input_type)

print("\n🚀 OLUŞTURULAN SONUÇ:\n")
print(sonuc)
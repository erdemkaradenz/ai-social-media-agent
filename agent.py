from scraper import scrape_url
from memory import retrieve_similar_styles
from llm_client import generate_text_ollama 

class ContentAgent:
    def __init__(self, vector_store):
        self.vector_store = vector_store

    def run(self, input_data: str, platform: str, input_type: str):
        
        raw_content = input_data
        current_temp = 0.7 
        
        if input_type == "url":
            print(f"🌍 URL taranıyor: {input_data}")
            scrape_result = scrape_url(input_data)
            if "Error" in scrape_result:
                return f"❌ Hata: {scrape_result}"
            raw_content = scrape_result
            current_temp = 0.1 
        

        search_query = raw_content[:200] if input_type == "url" else "teknoloji yazılım kariyer"
        examples = retrieve_similar_styles(self.vector_store, search_query)
        examples_text = "\n---\n".join(examples)

        task_instruction = ""
        
        if input_type == "url":
            task_instruction = f"""
            DURUM: Kullanıcı İngilizce/Türkçe bir teknik metin verdi.
            GÖREV: Bu metni {platform} için %100 Türkçe özetle.
            KURAL: Sadece metindeki bilgileri kullan. Dışarıdan ekleme yapma.
            """
        else:
            task_instruction = f"""
            DURUM: Kullanıcı senden şu konuda TÜRKÇE bir post istiyor: "{raw_content}"
            GÖREV: Kendi bilgi birikimini kullanarak bu isteği yerine getir.
            
            ADIMLAR:
            1. Konuyu (örn: RAG = Retrieval-Augmented Generation) doğru tanımla. Uydurma kısaltma kullanma.
            2. Neden önemli olduğunu vurgula.
            3. Okuyucuyu harekete geçirecek Türkçe bir cümle ile bitir.
            
            ⚠️ DİL KİLİDİ: Çıktı kesinlikle TÜRKÇE olacak. İngilizce yazmak YASAK.
            """

        final_prompt = f"""
        Rolün: Sen Türk bir Teknoloji Fenomenisin. Sadece TÜRKÇE konuşursun.
        
        {task_instruction}
        
        🛑 KIRMIZI ÇİZGİLER (ASLA İHLAL ETME):
        1. DİL: Ne olursa olsun cevap %100 TÜRKÇE olmalı. "It is...", "The combination..." gibi İngilizce cümleler KURMA.
        2. TEKRAR YOK: Aynı cümleleri kopyalayıp yapıştırma.
        3. FORMAT: Sadece post metnini yaz. JSON yok. Tırnak işareti yok.
        
        ###################
        STİL REHBERİ (SADECE TONU VE EMOJİ KULLANIMINI AL):
        {examples_text}
        ###################
        
        İŞLENECEK VERİ:
        {raw_content}
        
        TÜRKÇE POST METNİ (SADECE BURAYI YAZ):
        """

        print(f"✍️ Post yazılıyor... (Sıcaklık: {current_temp})")
        return generate_text_ollama(final_prompt, temperature=current_temp)
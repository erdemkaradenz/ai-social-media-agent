from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import ContentAgent
from memory import create_memory_index
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI(title="AI Social Media Content Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("⏳ Sistem Başlatılıyor... Hafıza yükleniyor...")
vector_store = create_memory_index()
agent = ContentAgent(vector_store)
print("✅ Sistem Hazır! API İstekleri Bekleniyor...")

# Veri Modeli
class GenerateRequest(BaseModel):
    input_data: str      
    input_type: str      
    platform: str        

@app.post("/generate")
async def generate_post(request: GenerateRequest):
    try:
        result = agent.run(
            input_data=request.input_data,
            platform=request.platform,
            input_type=request.input_type
        )
        return {"success": True, "content": result}
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.get("/")
def read_root():
    return {"message": "AI Agent API is running! 🚀"}
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from 'axios'
import ReactMarkdown from 'react-markdown' 

function App() {
  const [inputData, setInputData] = useState('')       
  const [inputType, setInputType] = useState('topic')  
  const [platform, setPlatform] = useState('twitter')  
  const [result, setResult] = useState('')             
  const [loading, setLoading] = useState(false)        
  const [error, setError] = useState('')               

  const handleGenerate = async () => {
    setLoading(true);
    setResult('');
    setError('');

    try {
      const response = await axios.post('http://127.0.0.1:8000/generate', {
        input_data: inputData,
        input_type: inputType,
        platform: platform
      });

      if (response.data.success) {
        setResult(response.data.content);
      } else {
        setError("Sunucu Hatası: " + response.data.error);
      }

    } catch (err) {
      console.error(err);
      setError("Bağlantı Hatası! Backend (uvicorn) çalışıyor mu?");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <header className="header">
        <h1>🤖 AI Social Media Agent</h1>
        <p>İçerik üretmenin en akıllı yolu.</p>
      </header>

      <div className="card">
        {/* AYARLAR KISMI */}
        <div className="controls">
          <div className="control-group">
            <label>Tür Seçin:</label>
            <select value={inputType} onChange={(e) => setInputType(e.target.value)}>
              <option value="topic">💡 Konu Başlığı</option>
              <option value="url">🌍 Web Sitesi (URL)</option>
            </select>
          </div>

          <div className="control-group">
            <label>Platform:</label>
            <select value={platform} onChange={(e) => setPlatform(e.target.value)}>
              <option value="twitter">🐦 Twitter (X)</option>
              <option value="linkedin">💼 LinkedIn</option>
            </select>
          </div>
        </div>

        {/* METİN GİRİŞ ALANI */}
        <textarea
          className="input-area"
          rows="4"
          placeholder={inputType === 'url' ? "https://ornek-makale.com..." : "Örn: RAG nedir, FastAPI avantajları..."}
          value={inputData}
          onChange={(e) => setInputData(e.target.value)}
        />

        {/* BUTON */}
        <button 
          className="generate-btn" 
          onClick={handleGenerate} 
          disabled={loading || !inputData}
        >
          {loading ? 'Yazıyor... ⏳' : '✨ İçerik Oluştur'}
        </button>

        {/* HATA MESAJI */}
        {error && <div className="error-box">{error}</div>}
      </div>

      {/* SONUÇ ALANI */}
      {result && (
        <div className="result-card">
          <h3>🚀 Oluşturulan Post:</h3>
          <div className="markdown-content">
            <ReactMarkdown>{result}</ReactMarkdown>
          </div>
          <button 
            className="copy-btn"
            onClick={() => navigator.clipboard.writeText(result)}
          >
            Kopyala
          </button>
        </div>
      )}
    </div>
  )
}

export default App

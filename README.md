# 🤖 AI Social Media Content Agent (RAG & LLM)

![Project Status](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![React](https://img.shields.io/badge/React-18-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED)
![AI Model](https://img.shields.io/badge/Model-Llama3-orange)

An end-to-end **Generative AI application** that automates the creation of professional social media posts (LinkedIn & Twitter). This project leverages **RAG (Retrieval-Augmented Generation)** to minimize hallucinations and maintain a consistent tone, orchestrated via a **FastAPI** backend and a modern **React** frontend.

---

## 🚀 Key Features

* **Retrieval-Augmented Generation (RAG):** Uses FAISS vector storage to retrieve relevant style examples, ensuring high-quality and context-aware outputs.
* **Local LLM Orchestration:** Runs entirely on local hardware using **Ollama (Llama 3)**, ensuring data privacy and zero API costs.
* **Full-Stack Architecture:** * **Backend:** Asynchronous FastAPI service handling scraping, embedding, and generation.
    * **Frontend:** Responsive React (Vite) interface with Dark Mode support.
* **Web Scraping:** Capable of extracting content from URLs to generate summary posts.
* **Dockerized Deployment:** Fully containerized architecture using Docker Compose for one-click deployment.

---

## 🛠️ Tech Stack

### Backend
* **Framework:** FastAPI (Python)
* **Vector Database:** FAISS (Facebook AI Similarity Search)
* **Scraping:** BeautifulSoup4
* **LLM Integration:** LangChain Concepts & Custom API Clients

### Frontend
* **Framework:** React.js (Vite)
* **Styling:** CSS3 (Custom Dark Mode)
* **HTTP Client:** Axios

### DevOps & AI
* **Containerization:** Docker & Docker Compose
* **Model Serving:** Ollama (Llama 3)

---

## 📸 Screenshots

*(You can add your screenshots here)*

---

## ⚙️ Installation & Setup

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
* [Ollama](https://ollama.com/) installed on your host machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/ai-social-media-agent.git](https://github.com/YOUR_USERNAME/ai-social-media-agent.git)
cd ai-social-media-agent
```

### 2. Pull the Llama 3 Model
Ensure Ollama is running on your host machine and pull the model:
```bash
ollama pull llama3
```

### 3. Run with Docker Compose
Build and start the services (Backend + Frontend):
```bash
docker-compose up --build
```

### 4. Access the Application
Open your browser and navigate to:
Frontend UI: http://localhost:5173
Backend API Docs: http://localhost:8000/docs
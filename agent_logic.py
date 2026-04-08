import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from tools import environmental_tools

load_dotenv()

def get_ecosync_agent():
    # Mengambil API key (mendukung GEMINI_API_KEY karena sebelumnya Anda menggunakan variabel tersebut)
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    
    if not api_key:
        raise ValueError("API Key belum dikonfigurasi. Buat file .env di folder EcoSync-Agent dan isi GEMINI_API_KEY=...")

    # Inisialisasi Gemini 2.5 Flash
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3, api_key=api_key)

    # Menggunakan LangGraph prebuilt yang merupakan standar baru di LangChain v0.3+
    agent = create_react_agent(llm, tools=environmental_tools)
    
    return agent
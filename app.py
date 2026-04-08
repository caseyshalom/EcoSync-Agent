import sqlite3
from flask import Flask, render_template, request, jsonify
from agent_logic import get_ecosync_agent

# Inisialisasi Basis Data (SQLite)
def init_db():
    conn = sqlite3.connect('ecosync_database.db', check_same_thread=False)
    c = conn.cursor()
    # Membuat tabel untuk menyimpan riwayat laporan dan chat
    c.execute('''
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            bot_response TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Jalankan inisiasi saat server Flask mulai
init_db()

app = Flask(__name__)
agent_executor = get_ecosync_agent()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_agent():
    user_input = request.json.get('message')
    try:
        # Agen mulai menalar dan memberikan jawaban
        result = agent_executor.invoke({"messages": [("user", user_input)]})
        response_content = result["messages"][-1].content
        
        # Pengecekan tipe data karena model terbaru terkadang mengembalikan list of objects
        if isinstance(response_content, list):
            texts = []
            for item in response_content:
                if isinstance(item, dict) and "text" in item:
                    texts.append(item["text"])
                elif isinstance(item, str):
                    texts.append(item)
            final_output = " ".join(texts)
        else:
            final_output = str(response_content)
            
        # Menyimpan percakapan ke dalam Basis Data
        conn = sqlite3.connect('ecosync_database.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('INSERT INTO chat_history (user_message, bot_response) VALUES (?, ?)', (user_input, final_output))
        conn.commit()
        conn.close()
            
        return jsonify({"status": "success", "output": final_output})
    except Exception as e:
        return jsonify({"status": "error", "output": f"[ERROR SYSTEM]: {str(e)}"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
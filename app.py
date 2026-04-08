from flask import Flask, render_template, request, jsonify
from agent_logic import get_ecosync_agent

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
            
        return jsonify({"status": "success", "output": final_output})
    except Exception as e:
        return jsonify({"status": "error", "output": f"[ERROR SYSTEM]: {str(e)}"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
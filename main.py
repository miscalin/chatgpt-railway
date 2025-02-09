from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Устанавливаем API-ключ OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/ask', methods=['POST'])
def ask_gpt():
    data = request.json
    prompt = data.get("prompt", "")

    response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

    return jsonify({"response": response["choices"][0]["message"]["content"]})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

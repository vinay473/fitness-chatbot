from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai

openai.api_key = "your_openai_api_key_here"

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI fitness coach. Give tips about fitness, workouts, and diet.",
            },
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
        max_tokens=150
    )

    reply = response.choices[0].message["content"].strip()
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True, port=5050)

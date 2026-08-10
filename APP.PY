from flask import Flask, render_template, request, jsonify
from chatbot import get_response
from database import init_db, save_chat, get_chat_history

app = Flask(__name__)

# Initialize database
init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({
            "success": False,
            "response": "Please enter a message."
        })

    bot_response = get_response(user_message)

    # Save conversation
    save_chat(user_message, bot_response)

    return jsonify({
        "success": True,
        "response": bot_response
    })


@app.route("/history")
def history():
    chats = get_chat_history()
    return render_template("history.html", chats=chats)


if __name__ == "__main__":
    app.run(debug=True)

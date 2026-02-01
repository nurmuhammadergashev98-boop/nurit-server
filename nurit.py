from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from datetime import datetime

app = Flask(__name__)
CORS(app)

TOKEN = "8487195167:AAFwvvhP78aiX0C25cTXCSXy-xOZpyrGt3A"
MY_ID = "5554634108"

@app.route('/send_message', methods=['POST'])
def handle_form():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    text = data.get('message')
    vaqt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 1. BAZAGA SAQLASH (Faylga yozish)
    with open("mijozlar.txt", "a", encoding="utf-8") as file:
        file.write(f"Vaqt: {vaqt} | Ism: {name} | Email: {email} | Xabar: {text}\n")
        file.write("-" * 50 + "\n")

    # 2. TELEGRAMGA YUBORISH
    message = f"🚀 YANGI BUYURTMA!\n\n👤 Mijoz: {name}\n📧 Email: {email}\n📝 Xabar: {text}\n⏰ Vaqt: {vaqt}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": MY_ID, "text": message})
    
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    print("Server yondi! Mijozlarni kutmoqdaman...")
    app.run(port=5000)
from flask import Flask, request, jsonify

app = Flask(__name__)

# 自動回覆霸凌相關訊息的邏輯
def bullying_reply(message):
message = message.lower()

if "霸凌" in message or "欺負" in message:
return "如果你在遭遇霸凌，我很願意聽你說。我希望你知道你值得被尊重，也絕對不是你的錯。"

if "被罵" in message:
return "被罵一定很難受吧？你可以跟我說更多，我會陪著你。"

if "怎麼辦" in message:
return "你不是一個人，我在這裡陪你。我們可以一起找出可以做的第一步，好嗎？"

# 預設回覆
return "我在聽喔，你可以跟我說發生了什麼事。"


@app.route("/reply", methods=["POST"])
def reply():
data = request.get_json()
user_message = data.get("message", "")
bot_response = bullying_reply(user_message)
return jsonify({"reply": bot_response})


@app.route("/")
def home():
return "Bullying Auto-Reply API is running."


if __name__ == "__main__":
app.run(host="0.0.0.0", port=10000)

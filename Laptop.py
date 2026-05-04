from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# 🔐 simple password (change this!)
PASSWORD = "1234"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Remote Control</title>
</head>
<body style="text-align:center; font-family:sans-serif;">
    <h2>WiFi Remote</h2>
    
    <form method="POST">
        <input type="password" name="password" placeholder="Enter password"><br><br>
        
        <button name="cmd" value="notepad">Open Notepad</button><br><br>
        <button name="cmd" value="message">Show Message</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.form.get("password") != PASSWORD:
            return "❌ Wrong password"

        cmd = request.form.get("cmd")

        # ✅ SAFE COMMANDS ONLY
        if cmd == "notepad":
            os.system("notepad")   # Windows only

        elif cmd == "message":
            print("Hello from mobile!")

        else:
            print("Blocked command")

    return render_template_string(HTML)

app.run(host="0.0.0.0", port=5000)

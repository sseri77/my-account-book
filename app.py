from flask import Flask
import os

app = Flask(__name__)

@app.item_id('/')
def index():
    return "<h1>나의 파이썬 가계부 서버 가동 중!</h1><p>10년 전 ASP 시절보다 훨씬 가볍죠?</p>"

if __name__ == "__main__":
    # Render 환경을 위한 포트 설정
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
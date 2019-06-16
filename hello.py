# coding: utf-8
from flask import Flask

# 利用するモジュールが1つだけなら'__name__'を使わなければいけない
# アプリケーションとしてインポートされるときは'__main__'らしい
app = Flask(__name__)

# routeデコーダでURLを指定する
@app.route('/')
def hello_world():
    return "Hello World!"

# Pythonインタプリタから直接実行されたときに
# アプリが実行されることを保証するための条件
if __name__ == '__main__':
    # 外部からアクセスを許可するための設定
    app.run(host='0.0.0.0')

    # アプリケーションの実行
    app.run()
    



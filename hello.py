# coding: utf-8
from flask import Flask

# 利用するモジュールが1つだけなら'__name__'を使わなければいけない
# アプリケーションとしてインポートされるときは'__main__'らしい
app = Flask(__name__)

# routeデコーダでURLを指定する
@app.route('/')
def index():
    return 'Index Page'

# ルーティングで切り替え
@app.route('/hello')
def hello_world():
# 始まりの関数
    return "Hello World!"

# Pythonインタプリタから直接実行されたときに
# アプリが実行されることを保証するための条件
if __name__ == '__main__':
    # 外部からアクセスを許可するための設定
    app.run(host='0.0.0.0')

    # デバッグモードを指定
    app.debug = True

    # アプリケーションの実行
    app.run()
    



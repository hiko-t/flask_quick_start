# coding: utf-8
from flask import Flask, render_template

# 利用するモジュールが1つだけなら'__name__'を使わなければいけない
# アプリケーションとしてインポートされるときは'__main__'らしい
app = Flask(__name__)

# routeデコーダでURLを指定する
@app.route('/')
def index():
    return 'Index Page'

# ルーティングで切り替え
@app.route('/hello/')
def hello_world(name=None):
    # 始まりの関数
    return 'Hello World'

# URLを変数名として扱う
@app.route('/user/<username>')
def show_user_profile(username):
    # 例）そのユーザのユーザプロフィールを表示する
    return 'User name is ' + username

# 型を指定して変数名を受け付ける
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 与えられた数値型のIDをポストに表示する
    pass

# 固有のURLによるリダイレクション
@app.route('/projects/')
def projects():
    # 末尾にスラッシュをあると
    # URL入力時にスラッシュが無くてもリダイレクトしてくれる
    return 'Projects Page'

@app.route('/about')
def about():
    # 末尾にスラッシュが無いと
    # URL入力時にスラッシュが無いと404エラーとなる
    # これはWerkzeugのルールに基づいている
    return 'About Page'

# HTTPメソッド
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

# スタティックファイル
# 動的なWebアプリを作る場合に必要な静的ファイルを呼び出す方法
# url_for('static', filename='style.css')
# あらかじめstaticという名前のフォルダを作っておけば
# そのフォルダに静的ファイルを作ってくれる


# Pythonインタプリタから直接実行されたときに
# アプリが実行されることを保証するための条件
if __name__ == '__main__':
    # 外部からアクセスを許可するための設定
    app.run(host='0.0.0.0')

    # デバッグモードを指定
    app.debug = True

    # アプリケーションの実行
    app.run()


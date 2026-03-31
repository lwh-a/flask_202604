from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_pybo():
    return 'Hello pybo!'

@app.route('/login')
def login():
    return '로그인 페이지 입니다.'

if __name__ == '__main__':
  app.run()



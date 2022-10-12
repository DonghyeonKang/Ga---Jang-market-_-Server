import flask

app = Flask(__name__)
app.secret_key = 'asd1inldap123jwaw'        # 세션을 암호화하기 위해 비밀키가 서명된 쿠키 사용
app.config.update(
			DEBUG = True,
			JWT_SECRET_KEY = "adswoern!@#rwlenf@#$13rweT#^DSfsrtwer"
		)
jwt = JWTManager(app)

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True, threaded=True)
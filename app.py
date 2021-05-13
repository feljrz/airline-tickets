from flask import Flask
from database import init_db
from routes import url_blueprint

app = Flask(__name__)
app.register_blueprint(url_blueprint)

init_db()

if __name__ == '__main__':
    app.run(debug=True, port = 5000)
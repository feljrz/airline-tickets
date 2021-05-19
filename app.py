from flask import Flask

from database import init_db
from routes import url_blueprint, login_manager

app = Flask(__name__)
app.register_blueprint(url_blueprint)
app.config['SECRET_KEY'] = 'hihihi'

init_db()

login_manager.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

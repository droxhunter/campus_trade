from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campus_trade.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Register blueprints
from routes.auth import auth_bp
from routes.products import product_bp
from routes.chat import chat_bp
from routes.admin import admin_bp
from routes.user import user_bp

app.register_blueprint(auth_bp)
app.register_blueprint(product_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from routes.auth import auth_bp
from routes.profile import profile_bp

app = Flask(__name__)

app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(profile_bp, url_prefix="/api/user")

if __name__ == "__main__":
    app.run(debug=True)

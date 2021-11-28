from flask import Flask, render_template
from blueprint.api.user import user_blueprint
app = Flask(__name__)
app.register_blueprint(user_blueprint)


@app.route("/")
def index():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
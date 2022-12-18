from flask import Blueprint, render_template
from model import User

index_bp = Blueprint("index", __name__)

@index_bp.route("/", methods=["GET","POST"])
@index_bp.route("/index", methods=["GET","POST"])
def index():
    user = User.query.all()
    return render_template("index.html", title="Index", user=user)
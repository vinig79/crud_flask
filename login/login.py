from flask import Blueprint
from flask import render_template
from login.form import Login


login_bp = Blueprint("login", __name__)


@login_bp.route("/login", methods=["GET","POST"])
def login():
    return "Login"
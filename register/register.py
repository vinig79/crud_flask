from flask import Blueprint
from register.form import Register

register_bp = Blueprint("register", __name__)

@register_bp.route("/register", methods=["GET","POST"])
def register():
    return "register"
from flask import Blueprint, render_template, redirect, flash, url_for
from main import db
from register.form import Register
from model import User

register_bp = Blueprint("register", __name__)

@register_bp.route("/register", methods=["GET","POST"])
def register():
    form = Register()
    if form.validate_on_submit():
        u = User(name=form.name.data, email=form.email.data, password=form.password.data)
        db.session.add(u)
        db.session.commit()
        flash(":)")
        return redirect(url_for('index.index'))
    return render_template("register.html", form=form)
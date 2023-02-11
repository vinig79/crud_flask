from flask import Blueprint, render_template, redirect, url_for, request
from model import User
from main import db
from index.form import Atualizar

index_bp = Blueprint("index", __name__)

@index_bp.route("/", methods=["GET","POST"])
@index_bp.route("/index", methods=["GET","POST"])
def index():
    user = User.query.all()
    return render_template("index.html", title="Index", user=user)

@index_bp.route("/delete", methods=["GET","POST"])
def delete():
    if request.method == "POST":
        a = request.form.getlist("id")
        print(a)
        for id in a:
            u = User.query.get(int(id))
            db.session.delete(u)
            db.session.commit()
    return redirect(url_for('index.index'))

@index_bp.route("/edit", methods=["GET","POST"])
def edit():
    form = Atualizar()
    if request.method == "POST":
        a = request.form.get("user_id")

    return render_template("atualiza.html", title="Atualiza", form=form)
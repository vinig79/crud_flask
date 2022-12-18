from main import db, login_mananger
from datetime import datetime
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def get_id(self):
        return self.id

@login_mananger.user_loader
def user_loader(id):
    return User.query.get(id)
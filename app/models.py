from app import db


class Statement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(100))

    def __repr__(self):
        return '<Statement {}>'.format(self.original)

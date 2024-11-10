from app import db


class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    github = db.Column(db.String(39))
    orcid = db.Column(db.String(19))
    affiliation = db.Column(db.String(100))
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    is_developer = db.Column(db.Boolean, default=False, nullable=False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

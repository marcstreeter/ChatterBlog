# Built-in
import datetime
import logging

# Module
from app import db
from app.config import config


logger = logging.getLogger(config.root_logger + __name__)


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    password = db.Column(db.String(100))
    #profile
    email = db.Column(db.String(120), unique=True)
    alias = db.relationship("Alias", backref="member")
    loc = db.relationship("Location", backref="member")
    reputation = db.relationship("Reputation", backref="member")
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    phone = db.Column(db.String(20))

    def __init__(self, username, password, email, name, phone):
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.phone = phone

    def __repr__(self):
        return '<User {username}({name})email:{email}>'.format(name=self.name, email=self.email, username=self.username)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'name': self.name,
            'bio': self.bio,
            'location': [loc.serialize for loc in self.loc],
            'tags': [tag.serialize for tag in self.tags],
            'phone': self.phone,
            'youtube': self.youtube,
            'payment': self.payment
        }

    def is_authenticated(self):
        return True if self.id else False
        #Returns True if the user is authenticated, i.e. they have provided valid credentials. (Only authenticated users will fulfill the criteria of login_required.)
    def is_active(self):
        return True
        #Returns True if this is an active user - in addition to being authenticated, they also have activated their account, not been suspended, or any condition your application has for rejecting an account. Inactive accounts may not log in (without being forced of course).
    def is_anonymous(self):
        return not self.is_authenticated()
        #Returns True if this is an anonymous user. (Actual users should return False instead.)
    def get_id(self):
        return self.id
        #Returns a unicode that uniquely identifies this user, and can be used to load the user from the user_loader callback. Note that this must be a unicode - if the ID is natively an int or some other type, you will need to convert it to unicode.


class Alias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey("Member.id", backref="alias"))


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float(precision=64), nullable=False)
    lon = db.Column(db.Float(precision=64), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('Member.id'), backref="location")


class Reputation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("Member.id"), backref="reputation")


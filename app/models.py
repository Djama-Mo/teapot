from application import db

from datetime import datetime


class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    action_id = db.Column(db.Integer, db.ForeignKey('action.id'))


class Action(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))

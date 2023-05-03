from app import db
from datetime import datetime


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable = True, default = None)
    is_complete = db.Column(db.Boolean, default = False)

    def to_dict(self):
        return {
            "id" : self.task_id,
            "title" : self.title,
            "description" : self.description,
            "is_complete" : self.is_complete
        }
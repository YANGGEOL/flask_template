from datetime import datetime

from App.exts import db


class Test(db.Model):
    """test table"""
    __tablename__ = 'tb_test'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(255), default='123456')
    email = db.Column(db.String(30), unique=True)
    is_delete = db.Column(db.Boolean, default=False)

    login_time = db.Column(db.DateTime, default=datetime.utcnow)
    created_time = db.Column(db.DateTime, default=datetime.utcnow)
    updated_time = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def as_dict(self):
        fields = ['id', 'username', 'password', 'email', 'is_delete', 'login_time', 'created_time', 'updated_time']
        return {field: getattr(self, field) for field in fields}

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()

# Database User
class User(db.Model, UserMixin):
    __tablename__ = "user_table"
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def get_id(self):
        """
        For use in flask login
        """
        return (self.id)

    def is_active(self):
        """
        For use in flask login
        """
        return (True)

    def is_authenticated(self):
        """
        For use in flask login
        """
        return super().is_authenticated

    def valid_login(email, password):
        users = User.query.all()
        for user in users:
            if user.email == email and user.password == password:
                return user
        return None
    

# Database Transport
class Transport(db.Model):
    __tablename__= 'transport_table'
    id = db.Column(db.Integer, primary_key=True)
    kms = db.Column(db.Float)
    transport = db.Column(db.String(50))
    fuel = db.Column(db.String(30))
    date = db.Column(db.DateTime, nullable=False)
    co2= db.Column(db.Float)
    ch4= db.Column(db.Float)
    total = db.Column(db.Float)  
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    def __init__(self, kms, transport, fuel, date, co2, ch4, total, user_id):
        self.kms = kms
        self.transport = transport
        self.fuel =fuel
        self.date = datetime.now()
        self.co2 =co2
        self.ch4 = ch4
        self.total = total
        self.user_id =user_id
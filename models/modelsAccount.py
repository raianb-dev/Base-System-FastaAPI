from email.policy import default
from sqlalchemy import Column, Integer, String, Float
import uuid


from dbconnection.connection import Base, engine, metadata

class Account(Base):
    __tablename__ = 'Account'
    id = Column(String(255), primary_key=True, default=uuid.uuid4)
    fullname = Column(String(255))
    username = Column(String(255))
    pwd = Column(String(255))
    
    def getAccount(self):
        return{
        'id': self.id,
        'username': self.username
        }
        
    def getById(self):
        return{
            'id':self.id,
            'fullname': self.fullname,
            'username': self.username
        }
        
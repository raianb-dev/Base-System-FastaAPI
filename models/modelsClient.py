import datetime
from sqlalchemy import Column, Integer, String, ForeignKey
import uuid

from dbconnection.connection import Base

class Client(Base):
    __tablename__ = 'cliente'
    id = Column(String(255), primary_key=True, default=uuid.uuid4)
    fullname = Column(String(255))
    cpf = Column(Integer)
    datanasc = Column(String(255))
    tel = Column(String(255))
    email = Column(String(255))
    address = Column(String(255))
    uf = Column(String(2))
    city = Column(String(255))
    
    def get(self):
        return {
            'id': self.id,
            'fullname': self. fullname
        }
    
    def get_byId(self):
        return {
            'id': self.id,
            'fullname': self.fullname,
            'cpf': self.cpf,
            'datanasc': self.datanasc,
            'tel': self.tel,
            'email': self.email,
            'address': self.address,
            'uf': self.city
        }
        
        
class NoteFiscal(Base):
    __tablename__='notefiscal'
    id = Column(String(255), primary_key=True)
    createat = Column(String(255), default=datetime.datetime.now())
    clientid = Column(String(255), ForeignKey('cliente.id'))
    
    def get(self, clientId=None, clientName=None):
        return {
            'id': self.id,
            'client': {
                'id': clientId,
                'name': clientName
            }
        }
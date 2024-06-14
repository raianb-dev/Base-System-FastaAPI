import datetime
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.orm import Session

from dbconnection.connection import Base

class Client(Base):
    __tablename__ = 'cliente'
    id = Column(String(255), primary_key=True, default=str(uuid.uuid4()))
    fullname = Column(String(255))
    cpf = Column(Integer)
    datanasc = Column(String(255))
    tel = Column(String(255))
    email = Column(String(255))
    address = Column(String(255))
    uf = Column(String(2))
    city = Column(String(255))

    orders = relationship("Orders", back_populates="client")
    resident = relationship("Resident", back_populates="client")

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

class Orders(Base):
    __tablename__='Orders'
    id = Column(String(255), primary_key=True, default=str(uuid.uuid4()))
    barcode = Column(String(255))
    date_in= Column(String(255))
    date_out= Column(String(255))
    image_url= Column(String(255))
    apto = Column(String(255))
    block = Column(String(255))
    status = Column(String(255))
    client_id = Column(String(255), ForeignKey('cliente.id'))

    client = relationship("Client", back_populates="orders")

    def get(self, db: Session):
            resident_name = None
            if self.apto and self.block:
                # Use a sessão do banco de dados passada como argumento
                resident = db.query(Resident).filter(Resident.apto == self.apto, Resident.block == self.block).first()
                if resident:
                    resident_name = resident.fullname
            return {
                'id': self.id,
                'barcode': self.barcode,
                'apto': self.apto,
                'block': self.block,
                'status': self.status,
                'date_in': self.date_in,
                'resident_name': resident_name
            }

    def get_byid(self):
        return {
            'id': self.id,
            'barcode': self.barcode,
            'date_in': self.date_in,
            'date_out': self.date_out,
            'image_url': self.image_url,
            'apto': self.apto,
            'block': self.block,
            'status': self.status,
            'clientId': self.client_id
        }

class Resident(Base):
    __tablename__ = 'resident'
    
    id = Column(String(255), primary_key=True, default=str(uuid.uuid4()))
    document = Column(String(255))
    fullname = Column(String(255))
    apto = Column(String(255))
    block = Column(String(255))
    phone = Column(String(255), default=None)
    email = Column(String(255))
    client_id = Column(String(255), ForeignKey('cliente.id'))

    client = relationship("Client", back_populates="resident")
    
    def get(self):
        return {
            "id": self.id,
            "fullname": self.fullname,
            "unidade":{
                "apto": self.apto,
                "block": self.block
            }
        }
    
    def getby_id(self):
        return {
            "id": self.id,
            "document": self.document,
            "fullname": self.fullname,
            "unidade":{
                "apto": self.apto,
                "block": self.block
            },
            "phone": self.phone,
            "email": self.email
            

        }
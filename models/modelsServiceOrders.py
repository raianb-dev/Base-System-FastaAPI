from sqlalchemy import Column, Integer, String, Float, Sequence, ForeignKey
from sqlalchemy.orm import relationship
import uuid, datetime


from dbconnection.connection import Base, engine, metadata


class ServiceOrdres(Base):
    
    __tablename__ = 'ServiceOrders'
    id = Column(String(255), primary_key=True, default=uuid.uuid4)
    number = Column(Integer, Sequence('OS', start=1, increment=1))
    typeId = Column(Column(Integer, ForeignKey('TypeServiceOrders.id')))
    typeserviceId = Column(Integer, ForeignKey('TypeService.id'))
    createdAt = Column(String(255), default=datetime.datetime.now())
    equipammentId = Column(Integer, ForeignKey('Equipament.id'))
    levelGravitId = Column(Integer, ForeignKey('LevelGravit.id'))
    description = Column(String(255))
    priority = Column(String(255))
    
    # many to one
    typeId = relationship('TypeServiceOrders')
    typeserviceId = relationship('TypeService')
    equipammentId = relationship('Equipamment')
    LevelGravit = relationship('Level')
    priority = relationship('Priority')
    
    def Get_byId(self):
        return{
            'id': self.id,
            'number': self.number,
            'typeId': self.typeId,
            'typeserviceId': self.typeserviceId,
            'createdAt': self.createdAt,
            'equipammentId': self.equipammentId,
            'levelGravitId': self.levelGravitId,
            'description': self.description,
            'priority': self.priority
        }
        
    def Get_Orders(self):
        return{
            'id': self.id,
            'number': self.number,
            'createdAt': self.createdAt,
            'levelGravitId': self.levelGravitId,
            'priority': self.priority  
        }
      
class TypeServiceOrders(Base):
    __tablename__ = 'TypeServiceOrders'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class TypeService(Base):
    __tablename__= 'TypeService'
    id = Column(Integer, primary_key= True)
    name = Column(String(255))
    
class Equipamment(Base):
    __tablename__= 'Equipament'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    
class Level(Base):
    __tablename__= 'LevelGravit'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class Priority(Base):
    __tablename__='Priority'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

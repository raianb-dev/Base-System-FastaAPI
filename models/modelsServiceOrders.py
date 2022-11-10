from sqlalchemy import Column, Integer, String, ForeignKey
import uuid, datetime

from dbconnection.connection import Base


class ServiceOrdres(Base):
    
    __tablename__ = 'service_orders'
    id = Column(String(255), primary_key=True, default=uuid.uuid4)
    number = Column(Integer)
    typeid = Column(Integer)
    typeserviceid = Column(Integer)
    createdat = Column(String(255), default=datetime.datetime.now())
    equipmmentid = Column(String(255), ForeignKey('equipmment.id'))
    levelgravitid = Column(Integer)
    description = Column(String(255))
    priority = Column(Integer)
    
    def Get_byId(self, equipmmentId, equipmmentName):
        return{
            'id': self.id,
            'number': self.number,
            'typeId': self.typeid,
            'typeserviceId': self.typeserviceid,
            'createdAt': self.createdat,
            'equipamment': {
                'id': equipmmentId,
                'name': equipmmentName
                },
            'levelGravitId': self.levelgravitid,
            'description': self.description,
            'priority': self.priority
        }
        
    def Get_Orders(self):
        return{
            'id': self.id,
            'number': self.number,
            'createdAt': self.createdat,
            'levelGravitId': self.levelgravitid,
            'priority': self.priority  
        }
      
class TypeServiceOrders(Base):
    __tablename__ = 'type_service_orders'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class TypeService(Base):
    __tablename__= 'type_service'
    id = Column(Integer, primary_key= True)
    name = Column(String(255))
    
class Equipmment(Base):
    __tablename__ = 'equipmment'
    id = Column(String(255), primary_key=True, default=uuid.uuid4)
    name = Column(String(255))
    def get(self):
        return{
            'id': self.id,
            'name': self.name
        }
    def getbyId(self):
        return{
            'id': self.id,
            'name': self.name
        }
class Level(Base):
    __tablename__= 'level_gravit'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class Priority(Base):
    __tablename__='priority'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

from sqlalchemy import Column, Integer, String, ForeignKey
import uuid


from dbconnection.connection import Base


class Statuses(Base):
    __tablename__ = 'statuses'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    subprocess = Column(String(255))
    
    def get(self):
        return {
            'id': self.id,
            'name': self.name,
            'subprocess': self.subprocess
        }
    
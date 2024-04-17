from sqlalchemy import Column, Integer, String, Boolean
import uuid, datetime

from dbconnection.connection import Base

class Email(Base):
    __tablename__ = 'SendersEmail'
    id = Column(String(255), primary_key=True, default=str(uuid.uuid4))
    apto = Column(String(255))
    block = Column(String(255))
    create_at = Column(String(255), default=str(datetime.datetime.now()))
    status = Column(Boolean, nullable=False)
    
    def get(self):
        return {
            "id": self.id,
            "unidade": {
                "apto": self.apto,
                "block": self.block
            },
            "create_at": self.create_at,
            "status": self.status
        }
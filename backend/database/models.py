from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class Weather(Base):
    __tablename__ = 'weather'

    timestamp = Column(Integer, primary_key=True, index=True)
    temperature = Column(Integer,index=True)
    moisture = Column(Integer, index=True)
    black_ice = Column(Boolean, index=True, default=False)
    cpu_temp = Column(Integer, index=True)

class Status(Base):
    __tablename__ = 'system_status'

    timestamp = Column(Integer, index=True)
    device_id = Column(String, primary_key= True, index=True)
    status = Column(String, index=True)

class ErrorLog(Base):
    __tablename__ = 'err_log'

    timestamp = Column(Integer, index=True)
    device_id = Column(String, primary_key= True, index=True)
    message = Column(String, index=True)


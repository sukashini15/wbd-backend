# models/case.py
from sqlalchemy import Column, Integer, String, Float
from database.db import Base

class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, autoincrement=True)
    area = Column(String, nullable=False)
    ph = Column(Float, nullable=False)
    turbidity = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
    rainfall = Column(Float, nullable=False)
    disease_reported = Column(String, nullable=False)

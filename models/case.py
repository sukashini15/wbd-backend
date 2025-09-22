# models/case.py
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.dialects.mysql import JSON
from database.db import Base

class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)                # links to user
    report_id = Column(String, nullable=False, unique=True)  # links multi-step submission
    symptoms = Column(JSON, nullable=True)                   # list of selected symptoms
    ph = Column(Float, nullable=True)
    turbidity = Column(Float, nullable=True)
    temperature = Column(Float, nullable=True)
    rainfall = Column(Float, nullable=True)
    disease_reported = Column(String, nullable=True)

from sqlalchemy import Column, Integer, String
from database import Base


class Foodstuff(Base):
    __tablename__ = "foodstuffs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    category = Column(String(30), index=True)
    proteins = Column(String(10))
    fats = Column(String(10))
    carbohydrates = Column(String(10))
    kcal = Column(String(10))
    
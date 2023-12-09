from pydantic import BaseModel


class Foodstuff(BaseModel):
    name: str
    category: str
    proteins: str
    fats: str
    carbohydrates: str
    kcal: str

    
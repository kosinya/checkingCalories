from dto import foodstuff
from models.foodstuff import Foodstuff
from sqlalchemy.orm import Session


# Получить все продукты
def get_all_foodstuffs(db: Session):
    return db.query(Foodstuff).all()


# Получить продукт по id
def get_foodstuff(id: int, db: Session):
    return db.query(Foodstuff).filter(Foodstuff.id == id).first()


# Добавить новый продукт
def create_foodstuff(data: foodstuff.Foodstuff, db: Session):
    new_foodstuff = Foodstuff(
        name=data.name,
        category=data.category,
        proteins=data.proteins,
        fats=data.fats,
        carbohydrates=data.carbohydrates,
        kcal=data.kcal
    )

    try:
        db.add(new_foodstuff)
        db.commit()
        db.refresh(new_foodstuff)
    except Exception as e:
        print(e)

    return new_foodstuff


# Удалить продукт по id
def delete_foodstuff(id: int, db: Session):
    fs = db.query(Foodstuff).filter(Foodstuff.id == id).delete()
    db.commit()
    return fs


# Обновить данные продукта по id
def update_foodstuff(data: foodstuff.Foodstuff, id: int, db: Session):
    fs = db.query(Foodstuff).filter(Foodstuff.id == id).first()

    fs.name = data.name
    fs.category = data.category
    fs.proteins = data.proteins
    fs.fats = data.fats
    fs.carbohydrates = data.carbohydrates
    fs.kcal = data.kcal

    try:
        db.add(fs)
        db.commit()
        db.refresh(fs)
    except Exception as e:
        print(e)

    return fs

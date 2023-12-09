from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_connection
from services import foodstuff as foodstuffService
from dto import foodstuff as foodstuffDto


routers = APIRouter()


@routers.post('/', tags=["foodstuff"])
async def create_foodstuff(data: foodstuffDto.Foodstuff = None, db: Session = Depends(get_connection)):
    return foodstuffService.create_foodstuff(data, db)


@routers.get('/all', tags=["foodstuff"])
async def get_all_foodstuffs(db: Session = Depends(get_connection)):
    return foodstuffService.get_all_foodstuffs(db)


@routers.get('/{id}', tags=["foodstuff"])
async def get_foodstuff(id: str = None, db: Session = Depends(get_connection)):
    return foodstuffService.get_foodstuff(int(id), db)


@routers.delete('/{id}', tags=["foodstuff"])
async def delete_foodstuff(id: str = None, db: Session = Depends(get_connection)):
    return foodstuffService.delete_foodstuff(int(id), db)


@routers.put('/{id}', tags=["foodstuff"])
async def update_foodstuff(data: foodstuffDto.Foodstuff = None, id: str = None, db: Session = Depends(get_connection)):
    return foodstuffService.update_foodstuff(data, int(id), db)

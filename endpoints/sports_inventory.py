from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_connect import SessionLocal, engine
from models.equip_model import Item, Base
from schemas.equip_schema import ItemBase, UpdateBase

Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/item/")
def add_item(item: ItemBase, db: Session = Depends(get_db)):
    try:
        items = db.query(Item).all()
        if item.name in items:
            raise HTTPException(status_code=400, detail="Item already exists")
        item = Item(name=item.name, quantity=item.quantity)
        db.add(item)
        db.commit()
        db.refresh(item)
        return {"message": "Item added successfully"}
    except Exception as e:
        return {"message": "Item already exist"}


@app.get("/items/")
def get_item(db: Session = Depends(get_db)):
    try:
        items = db.query(Item).all()
        if items is None:
            raise HTTPException(status_code=404, detail="Items not available")
        return items
    except Exception as e:
        return {"message": "Items not available"}


@app.put("/update/{item_id}/")
def update_item(item_id: int, up_item: UpdateBase, db: Session = Depends(get_db)):
    try:
        db_item = db.query(Item).filter(item_id == Item.id).first()
        print(db_item)
        if db_item is None:
            raise HTTPException(status_code=404, detail="Specified item not exist")
        db_item.quantity = up_item.quantity
        db.commit()
        db.refresh(db_item)
        return {"message": "Item updated successfully"}
    except Exception as e:
        print(e)
        return {"message": "Specified item not exist"}





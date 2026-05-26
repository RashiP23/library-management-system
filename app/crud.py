from sqlalchemy.orm import Session
from . import models, schemas

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    return db.query(models.Book).all()

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def update_book(db: Session, book_id: int, updated_book: schemas.BookCreate):
    book = get_book(db, book_id)

    if book:
        book.title = updated_book.title
        book.author = updated_book.author
        book.pages = updated_book.pages

        db.commit()
        db.refresh(book)

    return book

def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)

    if book:
        db.delete(book)
        db.commit()

    return book
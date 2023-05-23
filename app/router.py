from fastapi import APIRouter, HTTPException, status, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import BookSchema,RequestBook,Response
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar um livro
@router.post('/create')
async def create(request: RequestBook, db: Session = Depends(get_db)):
    crud.create_book(db, book=request.parameter)
    return Response(code=200,status="Sucesso",message="Livro criado com sucesso").dict(exclude_none=True)

# Listar todos os livros
@router.get('/', status_code=200, response_model=list[BookSchema])
async def get(db: Session = Depends(get_db)):
    _book = crud.get_book(db, 0, 100)
    return _book

# Listar um livro por id
@router.get('/{id}', status_code=201, response_model=BookSchema)
async def get_by_id(id:int, db: Session = Depends(get_db)):
    _book = crud.get_book_by_id(db,id)
    return _book

# Atualizar um livro
@router.post('/update')
async def create(request: RequestBook, db: Session = Depends(get_db)):
    _book = crud.update_book(db,book_id=request.parameter.id,title=request.parameter.title,description=request.parameter.description)
    return Response(code=200,status="Sucesso",message="Livro atualizado com sucesso", result=_book)

# Deletar um livro por id
@router.delete('{id}')
async def delete(id:int, db: Session = Depends(get_db)):
    crud.remove_book(db,book_id=id)
    return Response(code=200,status="Sucesso",message="Livro deletado com sucesso").dict(exclude_none=True)


from fastapi import FastAPI, HTTPException
from uuid import uuid4 as uuid

from models.itemModels import Obra
from routes.user import user

import uvicorn


# Aplicacion para agregar titulos literarios
#     Autor
#     nombre_libro
#     ano
#     genero
#     resumen
    
# Aplicacion realizada con fastapi y mysql

app = FastAPI()
app.include_router(user)


books = []

@app.post('/posts')
def to_register_book( obra : Obra ):
    obra.id= str(uuid())
    books.append(obra.dict())
    return books[-1]
    
@app.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in books:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Item not found")
    

    
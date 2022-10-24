from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import sqlite3


connection = sqlite3.connect("users.db")
cursor = connection.cursor() #com with db
cursor.execute("create table users (jmeno text, vek integer)")

user_list = [("Honza", 15),
             ("David", 18),
             ("Marie", 5),
             ("Filip", 13)]

cursor.executemany("insert into users values (?,?)", user_list)

app = FastAPI()

class Item(BaseModel):
    jmeno: str
    vek: int

@app.get("/{jmeno}")
async def hello(jmeno):
    user = cursor.execute("select * from users where jmeno=:a", {"a": f"{jmeno}"})
    return user

@app.get("/users")
async def hello():
    nupan = []
    for row in cursor.executemany("select * from users"):
        nupan.append(row)
    return nupan

@app.delete("/remove/{jmeno}")
async def delete(jmeno):
    cursor.execute("drop * from users where jmeno=:b", {"b": f"{jmeno}"})
    print("deleted")

@app.post("/register")
async def create_item(item: Item):
    items = jsonable_encoder(item)
    cursor.execute("insert * from users", items)
    print("insertion")

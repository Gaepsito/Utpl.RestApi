"""Código que permite la creación de una API RESTful con FastAPI para la 
   gestión de flotas de una empresa que alquila carros para conductores de Uber
"""
""" Pasos para ejecutar la aplicación:
    1. Ejecute el siguiente comando en una terminal para iniciar la aplicación
       uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    2. Vaya a PORTS y cambie el puerto 8000 de privado a público
    3. Forwarded Address le asignará una dirección, haga clic en Open in Browser
"""
# Declaración de librerías
# Inicialización de la aplicación FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Clase que define la estructura de un carro
class Car(BaseModel):
    id: int
    make: str
    model: str
    year: int
    driver: str

# Lista vacía para almacenar los carros creados.
cars_db = []

# Ruta para la página de inicio que devuelve un mensaje de bienvenida.
@app.get('/')
def bienvenida():
    return {'mensaje': 'Bienvenidos a la API de gestión de flotas - Alquiler de carros para conductores de Uber'}

# Ruta para obtener todos los carros almacenados en la lista.
# El parámetro "response_model" especifica que la respuesta será una lista de objetos "Car".
@app.get("/cars", response_model=List[Car])
async def leer_carros():
    return cars_db

# Ruta para crear un nuevo carro.
# El parámetro "response_model" especifica que la respuesta será un objeto "Car".
@app.post("/cars", response_model=Car)
async def crear_carro(car: Car):
    cars_db.append(car)  # Agrega el carro a la lista.
    return car

# Ruta para actualizar un carro existente por su ID.
# El parámetro "response_model" especifica que la respuesta será un objeto "Car".
@app.put("/cars/{car_id}", response_model=Car)
async def actualizar_carro(car_id: int, car: Car):
    for index, existing_car in enumerate(cars_db):
        if existing_car.id == car_id:
            cars_db[index] = car
            return car
    raise HTTPException(status_code=404, detail="Car not found")

# Ruta para eliminar un carro por su ID.
@app.delete("/cars/{car_id}")
async def eliminar_carro(car_id: int):
    for index, car in enumerate(cars_db):
        if car.id == car_id:
            del cars_db[index]
            return {"mensaje": "Carro eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Car not found")
"""Código que permite la creación de una API RESTful con FastAPI para la 
   gestión de flotas de una empresa que alquila carros para conductores de Uber
"""
""" Pasos para ejecutar la aplicación:
    1. Ejecute el siguiente comando en una terminal para iniciar la aplicación
       uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    2. Vaya a PORTS y cambie el puerto 8000 de privado a público
    3. Forwarded Address le asignará una dirección, haga clic en Open in Browser
"""
# Declaración de librerías
# Inicialización de la aplicación FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Clase que define la estructura de un carro
class Car(BaseModel):
    id: int
    make: str
    model: str
    year: int
    driver: str

# Lista vacía para almacenar los carros creados.
cars_db = []

# Ruta para la página de inicio que devuelve un mensaje de bienvenida.
@app.get('/')
def bienvenida():
    return {'mensaje': 'Bienvenidos a la API de gestión de flotas - Alquiler de carros para conductores de Uber'}

# Ruta para obtener todos los carros almacenados en la lista.
# El parámetro "response_model" especifica que la respuesta será una lista de objetos "Car".
@app.get("/cars", response_model=List[Car])
async def leer_carros():
    return cars_db

# Ruta para crear un nuevo carro.
# El parámetro "response_model" especifica que la respuesta será un objeto "Car".
@app.post("/cars", response_model=Car)
async def crear_carro(car: Car):
    cars_db.append(car)  # Agrega el carro a la lista.
    return car

# Ruta para actualizar un carro existente por su ID.
# El parámetro "response_model" especifica que la respuesta será un objeto "Car".
@app.put("/cars/{car_id}", response_model=Car)
async def actualizar_carro(car_id: int, car: Car):
    for index, existing_car in enumerate(cars_db):
        if existing_car.id == car_id:
            cars_db[index] = car
            return car
    raise HTTPException(status_code=404, detail="Car not found")

# Ruta para eliminar un carro por su ID.
@app.delete("/cars/{car_id}")
async def eliminar_carro(car_id: int):
    for index, car in enumerate(cars_db):
        if car.id == car_id:
            del cars_db[index]
            return {"mensaje": "Carro eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Car not found")

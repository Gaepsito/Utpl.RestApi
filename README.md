# API RESTful para la Gestión de Flotas de Carros

Esta es una API RESTful creada con FastAPI para la gestión de flotas de una empresa que alquila carros para conductores que trabajan con Uber.

## Pasos para ejecutar la aplicación

1. Ejecute el siguiente comando en una terminal para iniciar la aplicación:
   bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   
2. Vaya a PORTS y cambie el puerto 8000 de privado a público.
3. Forwarded Address le asignará una dirección, haga clic en "Open in Browser".

## Endpoints de la API

### Ruta de bienvenida

- *GET /*

  Devuelve un mensaje de bienvenida.

  *Respuesta:*
  json
  {
    "mensaje": "Bienvenidos a la API de gestión de flotas - Alquiler de carros para conductores de Uber"
  }
  

### Obtener todos los carros

- *GET /cars*

  Devuelve una lista de todos los carros.

  *Respuesta:*
  json
  [
    {
      "id": 1,
      "make": "Toyota",
      "model": "Corolla",
      "year": 2020,
      "driver": "Juan Perez"
    },
    ...
  ]
  

### Obtener un carro por ID

- *GET /cars/{car_id}*

  Devuelve un carro específico por su ID.

  *Parámetros:*
  - car_id (int): ID del carro.

  *Respuesta:*
  json
  {
    "id": 1,
    "make": "Toyota",
    "model": "Corolla",
    "year": 2020,
    "driver": "Juan Perez"
  }
  

### Crear un nuevo carro

- *POST /cars*

  Crea un nuevo carro.

  *Cuerpo de la solicitud:*
  json
  {
    "id": 1,
    "make": "Toyota",
    "model": "Corolla",
    "year": 2020,
    "driver": "Juan Perez"
  }
  

  *Respuesta:*
  json
  {
    "id": 1,
    "make": "Toyota",
    "model": "Corolla",
    "year": 2020,
    "driver": "Juan Perez"
  }
  

### Actualizar un carro existente

- *PUT /cars/{car_id}*

  Actualiza la información de un carro existente.

  *Parámetros:*
  - car_id (int): ID del carro.

  *Cuerpo de la solicitud:*
  json
  {
    "id": 1,
    "make": "Toyota",
    "model": "Corolla",
    "year": 2020,
    "driver": "Juan Perez"
  }
  

  *Respuesta:*
  json
  {
    "id": 1,
    "make": "Toyota",
    "model": "Corolla",
    "year": 2020,
    "driver": "Juan Perez"
  }
  

### Eliminar un carro

- *DELETE /cars/{car_id}*

  Elimina un carro por su ID.

  *Parámetros:*
  - car_id (int): ID del carro.

  *Respuesta:*
  json
  {
    "mensaje": "Carro eliminado"
  }
  

## Modelo de Datos

### Car

- id (int): Identificador único del carro.
- make (str): Marca del carro.
- model (str): Modelo del carro.
- year (int): Año del carro.
- driver (str): Nombre del conductor asignado al carro.

## Notas

- Para actualizar o eliminar un carro, se utiliza la posición en la lista cars_db, no el ID del objeto.
- Esta API es una simulación y utiliza una lista en memoria (cars_db) como base de datos.

# vamos a definir el esquema de datos para los productos y validaciones 

from pydantic import BaseModel, Field, field_validator
from datetime import datetime, date
from uuid import UUID


def validar_fecha_creacion(value: date) -> date:  
    # funcion para validar que la fecha de creacion no sea menor a la fecha actual
    if value < date.today():  
        raise ValueError("La fecha de creacion no puede ser menor a la fecha actual.")
    return value


class ProductCreate(BaseModel):
    id_categoria: UUID
    nombre: str = Field(min_length=3, max_length=200)
    descripcion: str | None = Field(default=None, max_length=300)
    precio: float = Field(gt=0)
    stock: int = Field(ge=0)
    imagen_url: str | None = Field(default=None, max_length=200)
    tags: list[str] | None = Field(default=None)
    activo: bool = Field(default=True)
    fecha_creacion: datetime = Field(default_factory=datetime.now)


    @field_validator("ingreso_date")
    @classmethod
    def validar_fecha_creacion(cls, value: date) -> date:
        return validar_fecha_creacion(value)


class ProductUpdate(BaseModel):
    id_categoria: UUID | None = Field(default=None)
    nombre: str | None = Field(default=None, min_length=3, max_length=200)
    descripcion: str | None = Field(default=None, max_length=300)
    precio: float | None = Field(default=None, gt=0)
    stock: int | None = Field(default=None, ge=0)
    imagen_url: str | None = Field(default=None, max_length=200)
    tags: list[str] | None = Field(default=None)
    activo: bool | None = Field(default=None)
    fecha_creacion: datetime | None = Field(default=None)

    @field_validator("fecha_creacion")
    @classmethod
    def validar_fecha_creacion(cls, value: datetime | None) -> datetime | None:
        if value is None:
            return value    
            
        return validar_fecha_creacion(value)


class ProductOut(BaseModel):
    id: UUID
    id_categoria: UUID
    nombre: str
    descripcion: str | None = Field(default=None)
    precio: float
    stock: int
    imagen_url: str | None = Field(default=None)
    tags: list[str] | None = Field(default=None)
    activo: bool
    fecha_creacion: datetime
    
    class Config:
        orm_mode = True


class ProductList(BaseModel):
    total: int
    items: list[ProductOut]


class OneProduct(BaseModel):
    items: list[ProductOut]
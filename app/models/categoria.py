from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from uuid import UUID

def validar_fecha_creacion(value: datetime) -> datetime:
    # funcion para validar que la fecha de creación no sea mayor a la fecha actual
    if value > datetime.now():
        raise ValueError("La fecha de creación no puede ser mayor a la fecha actual.")
    return value

class categoriaCreate(BaseModel):
    nombre: str = Field(min_length=3, max_length=100)
    descripcion: str | None = Field(default=None, max_length=300)
    fecha_creacion: datetime = Field(default_factory=datetime.now)

    @field_validator("fecha_creacion")
    @classmethod
    def validar_fecha_creacion(cls, value: datetime) -> datetime:
        return validar_fecha_creacion(value)

class categoriaUpdate(BaseModel):
    nombre: str | None = Field(default=None, min_length=3, max_length=100)
    descripcion: str | None = Field(default=None, max_length=300)
    fecha_creacion: datetime | None = Field(default=None)

    @field_validator("fecha_creacion")
    @classmethod
    def validar_fecha_creacion(cls, value: datetime) -> datetime:
        return validar_fecha_creacion(value)
    
    
class categoriaOut(BaseModel):
    id: int
    nombre: str | None= Field(default=None, min_length=3, max_length=200) 
    descripcion: str | None= Field(default=None, min_length=3, max_length=200) 
    fecha_creacion: datetime | None = Field(default=None)


    class Config:
        orm_mode = True


class categoriaList(BaseModel):
    total: int
    items: list[categoriaOut]

class OnecategoriaOut(BaseModel):
    items: list[categoriaOut]
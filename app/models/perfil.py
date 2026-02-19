from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from uuid import UUID
from typing import Optional, List

def validar_fecha_registro(value: datetime) -> datetime:
    # funcion para validar que la fecha de registro no sea mayor a la fecha actual
    if value > datetime.now():
        raise ValueError("La fecha de registro no puede ser mayor a la fecha actual.")
    return value

class perfilCreate(BaseModel):
    nombre_usuario: str = Field(min_length=3, max_length=50)
    telefono: str = Field(min_length=10, max_length=15)
    fecha_registro: datetime = Field(default_factory=datetime.now)
    rol: str = Field(min_length=3, max_length=50)
    contrasena: str = Field(min_length=6)


   
    @field_validator("fecha_registro")
    @classmethod
    def validar_fecha_registro(cls, value: datetime) -> datetime:
        return validar_fecha_registro(value)


class perfilUpdate(BaseModel):
    nombre_usuario: str | None = Field(default=None, min_length=3, max_length=50)
    telefono: str | None = Field(default=None, min_length=10, max_length=15)
    fecha_registro: datetime | None = Field(default=None)
    rol: str | None = Field(default=None, min_length=3, max_length=50)
    contrasena: str | None = Field(default=None, min_length=6)

    
    @field_validator("fecha_registro")
    @classmethod
    def validar_fecha_registro(cls, value: datetime) -> datetime:
        return validar_fecha_registro(value)


class perfilOut(BaseModel):
    id: UUID
    nombre_usuario: str
    telefono: str
    fecha_registro: datetime
    rol: str
    contrasena: str

    class Config:
        orm_mode = True


class perfilList(BaseModel):
    total: int
    items: list[perfilOut]
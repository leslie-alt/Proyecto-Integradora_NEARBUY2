from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from uuid import UUID
from typing import Optional, List

def validar_fecha_ingreso(value: datetime) -> datetime:
    # funcion para validar que la fecha de ingreso no sea mayor a la fecha actual
    if value > datetime.now():
        raise ValueError("La fecha de ingreso   no puede ser mayor a la fecha actual.")
    return value

class perfilCreate(BaseModel):
    nombre_completo: str = Field(min_length=3, max_length=100)
    telefono: str = Field(min_length=7, max_length=15)
    fecha_ingreso: datetime = Field(default_factory=datetime.now)
    rol: str = Field(min_length=3, max_length=50)

    @field_validator("fecha_ingreso")
    @classmethod
    def validar_fecha_ingreso(cls, value: datetime) -> datetime:
        return validar_fecha_ingreso(value)


class perfilUpdate(BaseModel):
    perfilname: str | None = Field(default=None, min_length=3, max_length=50)
    email: str | None = Field(default=None, min_length=5, max_length=150)
    password: str | None = Field(default=None, min_length=6)

    
    @field_validator("fecha_ingreso")
    @classmethod
    def validar_fecha_ingreso(cls, value: datetime) -> datetime:
        return validar_fecha_ingreso(value)


class perfilOut(BaseModel):
    id: UUID
    perfilname: str
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class perfilList(BaseModel):
    total: int
    items: list[perfilOut]
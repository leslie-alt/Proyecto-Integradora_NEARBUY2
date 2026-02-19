
from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from uuid import UUID
from typing import Optional, List

def validar_fecha_creacion(value: datetime) -> datetime:
    # funcion para validar que la fecha de creación no sea mayor a la fecha actual
    if value > datetime.now():
        raise ValueError("La fecha de creación no puede ser mayor a la fecha actual.")
    return value

class PedidoCreate(BaseModel):
    id_usuario: UUID
    total: float = Field(gt=0)
    estatus: str = Field(min_length=3, max_length=50)
    metodo_pago: str = Field(min_length=3, max_length=50)
    codigo_qr: str | None = Field(default=None, max_length=200)
    fecha_creacion: datetime = Field(default_factory=datetime.now)
    id_empleado_prepara: UUID | None = Field(default=None)
    id_empleado_entrega: UUID | None = Field(default=None)

    @field_validator("fecha_creacion")
    @classmethod
    def validar_fecha_creacion(cls, value: datetime) -> datetime:
        return validar_fecha_creacion(value)
    

    
class PedidoUpdate(BaseModel):
    id_usuario: UUID | None = Field(default=None)
    total: float | None = Field(default=None, gt=0)
    estatus: str | None = Field(default=None, min_length=3, max_length=50)
    metodo_pago: str | None = Field(default=None, min_length=3, max_length=50)
    codigo_qr: str | None = Field(default=None, max_length=200)
    fecha_creacion: datetime | None = Field(default=None)
    id_empleado_prepara: UUID | None = Field(default=None)
    id_empleado_entrega: UUID | None = Field(default=None)

    @field_validator("fecha_creacion")
    @classmethod
    def validar_fecha_creacion(cls, value: datetime) -> datetime:
        return validar_fecha_creacion(value)


class PedidoOut(BaseModel):
    id: int
    id_usuario: int
    total: float
    estatus: str
    metodo_pago: str
    codigo_qr: str | None = Field(default=None)
    fecha_creacion: datetime
    id_empleado_prepara: UUID | None = Field(default=None)
    id_empleado_entrega: UUID | None = Field(default=None)
    
    class Config:
        from_attributes = True


class PedidoList(BaseModel):
    total: int
    items: List[PedidoOut]
from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from uuid import UUID



class detalle_pedidoCreate(BaseModel):
    id_pedido: int
    id_producto: int
    cantidad: int = Field(gt=0)
    precio_unitario: float = Field(gt=0)


class detalle_pedidoUpdate(BaseModel):
    id_pedido: UUID | None = Field(default=None)
    id_producto: UUID | None = Field(default=None)
    cantidad: int | None = Field(default=None, gt=0)
    precio_unitario: float | None = Field(default=None, gt=0)
    
    
class detalle_pedidoOut(BaseModel):
    id: int
    id_pedido: int | None = Field(default=None)
    id_producto: int | None = Field(default=None)
    cantidad: int | None = Field(default=None, gt=0)
    precio_unitario: float | None = Field(default=None, gt=0)
    class Config:
        orm_mode = True


class detalle_pedidoList(BaseModel):
    total: int
    items: list[detalle_pedidoOut]

class Onedetalle_pedidoOut(BaseModel):
    items: list[detalle_pedidoOut]
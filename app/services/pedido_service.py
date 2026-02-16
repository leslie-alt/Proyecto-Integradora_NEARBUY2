from uuid import UUID  #uuis es un identificador único universal, se utiliza para identificar de manera única un producto en la base de datos
from datetime import date
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import get_supabase_client
from app.core.config import config
from postgrest import CountMethod

def _table():
    sb = get_supabase_client()
    return sb.table(config.supabase_table)

def list_pedidos(skip: int = 0, limit: int = 100):
    try:
        res=_table().select("*", count=CountMethod.exact).range(skip, skip + limit - 1).execute()
        if not res.data:
            raise HTTPException(status_code=500, detail=f"Error al mostar los registros{e}")
        return {"items": res.data , "total": res.count or 0}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al mostar los registros{e}")
    
def get_pedido(pedido_id: UUID):
    try:
        res=_table().select("*").eq("id", str(pedido_id)).execute()
        if not res.data:
            raise HTTPException(status_code=404, detail="Pedido no encontrado")
        return {"item": res.data[0] if res.data else None}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener el pedido{e}")

def create_pedido(datos: dict):
    try:
        if not datos:
            raise HTTPException(status_code=500, detail=f"Error al crear el pedido{e}")
        datos=jsonable_encoder(datos)
        res=_table().insert(jsonable_encoder(datos)).execute()
        return res.data[0] if res.data else None
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el pedido{e}")

def update_pedido(pedido_id: UUID, datos: dict):
    try:
        if not datos:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el pedido{e}")
        datos=jsonable_encoder(datos)
        res=_table().update(jsonable_encoder(datos)).eq("id", str(pedido_id)).execute()
        if not res.data:
            raise HTTPException(status_code=404, detail="Pedido no encontrado")
        return res.data[0] if res.data else None
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el pedido{e}")
    
def delete_pedido(pedido_id: UUID):
    try:
        res=_table().delete().eq("id", str(pedido_id)).execute()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el pedido{e}")
    
    
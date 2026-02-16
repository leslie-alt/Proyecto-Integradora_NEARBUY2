
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

def list_categorias(skip: int = 0, limit: int = 100):
    
    try:
        res=_table().select("*", count=CountMethod.exact).range(skip, skip + limit - 1).execute()
        if not res.data:
            raise HTTPException(status_code=500, detail=f"Error al mostar los registros{e}")
        return {"items": res.data , "total": res.count or 0}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al mostar los registros{e}")
    
def get_categoria(categoria_id: UUID):
    try:
        res=_table().select("*").eq("id", str(categoria_id)).execute()
        if not res.data:
            raise HTTPException(status_code=404, detail="Categoria no encontrada")
        return {"item": res.data[0] if res.data else None}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener la categoria{e}")

def create_categoria(datos: dict):
    try:
        if not datos:
            raise HTTPException(status_code=500, detail=f"Error al crear la categoria{e}")
        datos=jsonable_encoder(datos)
        res=_table().insert(jsonable_encoder(datos)).execute()
        return res.data[0] if res.data else None
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear la categoria{e}")
    
def update_categoria(categoria_id: UUID, datos: dict):
    try:
        if not datos:
            raise HTTPException(status_code=500, detail=f"Error al actualizar la categoria{e}")
        datos=jsonable_encoder(datos)
        res=_table().update(jsonable_encoder(datos)).eq("id", str(categoria_id)).execute()
        if not res.data:
            raise HTTPException(status_code=404, detail="Categoria no encontrada")
        return res.data[0] if res.data else None
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar la categoria{e}")

def delete_categoria(categoria_id: UUID):
    try:
        res=_table().delete().eq("id", str(categoria_id)).execute()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar la categoria{e}")
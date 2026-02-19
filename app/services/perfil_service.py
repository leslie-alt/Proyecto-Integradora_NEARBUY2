

from uuid import UUID  #uuis es un identificador único universal, se utiliza para identificar de manera única un producto en la base de datos
from datetime import date
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import get_supabase_client
from app.core.config import config
from postgrest import CountMethod

def _table():
    sb = get_supabase_client()
    return sb.table("perfiles")

def list_perfil(skip: int = 0, limit: int = 100):
    
    try:
        res=_table().select("*", count=CountMethod.exact).range(skip, skip + limit - 1).execute()
        if not res.data:
            raise HTTPException(status_code=500, detail=f"Error al mostar los registros{e}")
        return {"items": res.data , "total": res.count or 0}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al mostar los registros{e}")
    
def get_perfil(perfil_id: UUID):
    try:
        res=_table().select("*").eq("id", str(perfil_id)).execute()
        if not res.data:
            raise HTTPException(status_code=404, detail="perfil no encontrado")
        return {"item": res.data[0] if res.data else None}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener el perfil{e}")

def create_perfil(datos: dict):
    try:
        if not datos:
            raise HTTPException(status_code=500, detail=f"Error al crear el perfil{e}")
        datos=jsonable_encoder(datos)
        res=_table().insert(jsonable_encoder(datos)).execute()
        return res.data[0] if res.data else None
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el perfil{e}")
    

def update_perfil(perfil_id: UUID, datos: dict):
    try:
        if not datos:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el perfil{e}")
        datos=jsonable_encoder(datos)
        res=_table().update(jsonable_encoder(datos)).eq("id", str(perfil_id)).execute()
        if not res.data:
            raise HTTPException(status_code=404, detail="perfil no encontrado")
        return res.data[0] if res.data else None
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el perfil{e}")
    
def delete_perfil(perfil_id: UUID):
    try:
        res=_table().delete().eq("id", str(perfil_id)).execute()
        if not res.data:
            raise HTTPException(status_code=404, detail="perfil no encontrado")
        return res.data[0] if res.data else None
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el perfil{e}")
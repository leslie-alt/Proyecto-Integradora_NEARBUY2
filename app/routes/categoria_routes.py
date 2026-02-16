
from fastapi import APIRouter, Path, Query
from uuid import UUID
from app.models.producto import categoriaCreate, categoriaOut, categoriaUpdate, categoriaList, OnecategoriaOut
from app.services.categoria_service import create_categoria, get_categoria, list_categoria, delete_categoria, update_categoria

router = APIRouter(prefix="/categorias", tags=["categorias"])

@router.post("", name="listar categorias", response_model=categoriaOut)
@router.get("/", name="listar_categorias_slash")
def listar_categorias(limit: int = Query(0, ge=0), offset: int = Query(100, ge=1)):
    return list_categoria(limit, offset)

@router.get("/{categoria_id}", name="obtener categoria", response_model=categoriaOut)
def obtener_categoria(categoria_id: UUID = Path(...)):
        return get_categoria(categoria_id)

@router.post("", name="crear categoria", response_model=categoriaOut)
@router.post("/", name="crear_categoria_slash", response_model=categoriaOut)
def crear_categoria(body: categoriaCreate):
    return create_categoria(body.model_dump())

@router.delete("/{categoria_id}", name="eliminar categoria")
def eliminar_categoria(categoria_id: UUID = Path(...)):
    return delete_categoria(categoria_id)

@router.put("/{categoria_id}", name="actualizar categoria", response_model=categoriaOut)
def actualizar_categoria(categoria_id: UUID = Path(...), body: categoriaUpdate = None):
    return update_categoria(categoria_id, body.model_dump(exclude_unset=True))

from fastapi import APIRouter, Path, Query
from uuid import UUID
from app.models.perfil import perfilOut, perfilCreate, perfilUpdate, perfilList
from app.services.perfil_service   import list_perfil, get_perfil, create_perfil, update_perfil, delete_perfil

router = APIRouter(prefix="/perfil", tags=["perfil"])

@router.get("", name="listar_perfil")
@router.get("/", name="listar_perfiles_slash")
def listar_perfiles(
    limit: int = Query(100, ge=1, le=200),
    offset: int = Query(0, ge=0),
):
    return list_perfil(limit, offset)


@router.get("/{perfil_id}", response_model=perfilOut, name="obtener_perfil")
def api_get_perfil(perfil_id: UUID = Path(...)):
    return get_perfil(perfil_id)

@router.post("", response_model=perfilOut, name="crear_perfil")
@router.post("/", response_model=perfilOut, name="crear_perfil_slash")
def api_create_perfil(body: perfilCreate):
    return create_perfil(body.model_dump())


@router.delete("/{perfil_id}", name="eliminar_perfil")
def api_delete_perfil(perfil_id: UUID):
    return delete_perfil(perfil_id)

@router.put("/{perfil_id}", response_model=perfilOut, name="actualizar_perfil")
def api_update_perfil(perfil_id: UUID, body: perfilUpdate):
    return update_perfil(perfil_id, body.model_dump())

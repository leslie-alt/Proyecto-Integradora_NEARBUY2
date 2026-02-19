from fastapi import APIRouter, Path, Query
from uuid import UUID
from app.models.pedido import  PedidoCreate, PedidoUpdate, PedidoOut
from app.services.pedido_service import create_pedido, delete_pedido, get_pedido, list_pedidos, update_pedido



router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@router.get("/", name= "Listar_pedidos", response_model=dict) # El response_model se establece como dict porque la función list_pedidos devuelve un diccionario con los items y el total
@router.get("/", name= "listar_pedidos_slash", response_model=dict) # El response_model se establece como dict porque la función get_pedido devuelve un diccionario con el item
def listar_pedidos(limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0)):
    return list_pedidos(limit, offset)

@router.get("/{pedido_id}", response_model=PedidoOut, name="obtener_pedido") # El response_model se establece como dict porque la función get_pedido devuelve un diccionario con el item
def api_get_pedido(pedido_id: UUID = Path(...)):
    return get_pedido(pedido_id)

@router.post("/", response_model=PedidoOut, name="crear_pedido")
@router.post("/", response_model=PedidoOut, name="crear_pedido_slash")
def api_create_pedido(body: PedidoCreate):
    return create_pedido(body.model_dump())

@router.delete("/{pedido_id}", name="eliminar_pedido")
def api_delete_pedido(pedido_id: UUID ):
    return delete_pedido(pedido_id)

@router.put("/{pedido_id}", response_model=PedidoOut, name="actualizar_pedido")
def api_update_pedido(pedido_id: UUID, body: PedidoUpdate):
    return update_pedido(pedido_id, body.model_dump(exclude_unset=True))
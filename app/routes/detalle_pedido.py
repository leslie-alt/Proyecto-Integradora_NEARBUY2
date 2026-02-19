
from fastapi import APIRouter, Path, Query
from uuid import UUID
from app.services.detalle_pedido_service import list_detalle_pedidos, get_detalle_pedido, create_detalle_pedido, update_detalle_pedido, delete_detalle_pedido
from app.models.detalle_pedido import detalle_pedidoCreate, detalle_pedidoOut, detalle_pedidoUpdate


router= APIRouter(prefix="/detalle_pedido", tags=["detalle_pedido"])

@router.get("/", name="listar_detallePedidos") 
@router.get("/", name="listar_detallePedidos_slash")
def listar_detalle_pedidos(limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0)):
    return list_detalle_pedidos(offset, limit)

@router.get("/{detalle_pedido_id}", name="obtener_detalle_pedido", response_model=detalle_pedidoOut)
def api_obtener_detalle_pedido(detalle_pedido_id: UUID = Path(...)):
    return get_detalle_pedido(detalle_pedido_id)

@router.post("/", name="crear_detalle_pedido", response_model=detalle_pedidoOut)
@router.post("/", name="crear_detalle_pedido_slash", response_model=detalle_pedidoOut)
def api_crear_detalle_pedido(body: detalle_pedidoCreate):
    return create_detalle_pedido(body.model_dump())

@router.put("/{detalle_pedido_id}", name="actualizar_detalle_pedido", response_model=detalle_pedidoOut)
def api_actualizar_detalle_pedido(detalle_pedido_id: UUID = Path(...), body: detalle_pedidoUpdate = ...):
    return update_detalle_pedido(detalle_pedido_id, body.model_dump())

@router.delete("/{detalle_pedido_id}", name="eliminar_detalle_pedido")
def api_eliminar_detalle_pedido(detalle_pedido_id: UUID = Path(...)):
    
    return delete_detalle_pedido(detalle_pedido_id)
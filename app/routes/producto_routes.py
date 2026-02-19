
from unittest import skip
from fastapi import APIRouter, Path, Query
from uuid import UUID
from app.models.producto import ProductoCreate, ProductoOut
from app.services.producto_service import list_producto, get_producto, create_producto, update_producto, delete_producto

router = APIRouter(prefix="/productos", tags=["productos"])


@router.get("", name="listar_productos")
@router.get("/", name="listar_productos_slash")
def listar_productos(
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0)
):
    return list_producto(limit, offset)


@router.get("/{product_id}", response_model=ProductoOut, name="obtener_producto")
def api_get_product(product_id: UUID = Path(...)):
    return get_producto(product_id)

@router.post("", response_model=ProductoOut, name="crear_producto")
@router.post("/", response_model=ProductoOut, name="crear_producto_slash")
def api_create_product(body: ProductoCreate):
    return create_producto(body.model_dump())


@router.delete("/{product_id}", name="eliminar_producto")
def api_delete_product(product_id: UUID):
    return delete_producto(product_id)

@router.put("/{product_id}", response_model=ProductoOut, name="actualizar_producto")
def api_update_product(product_id: UUID, body: ProductoCreate):
    return update_producto(product_id, body.model_dump())

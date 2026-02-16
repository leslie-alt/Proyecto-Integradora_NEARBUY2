from fastapi import HTTPException, status

def not_found(entity: str):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{entity} no encontrado"
    )


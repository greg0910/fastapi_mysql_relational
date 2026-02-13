from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from ..models.user import User, Perfil
from ..schemas.user import UsuarioCreate, UsuarioRead,UsuarioPut
from ..db.db import get_db
from ..security.security import hash_password

router = APIRouter()

@router.get("/")
def bienvenida():
    return {"message": "Hola mi primer CRUD con MYSQL"}

@router.post("/User_create", response_model=UsuarioRead)
def post_user(payload: UsuarioCreate, db: Session = Depends(get_db)):
    user = User(
        correo=payload.email,
        password=hash_password(payload.password)
        )
    perfil = Perfil(
        nombre=payload.nombre,
        apellido=payload.apellido,
        telefono=payload.telefono
    )
    
    user.perfil = perfil

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409,detail="El correo ya está registrado")
    
    return UsuarioRead(
        id=user.id_usuario,
        nombre=user.perfil.nombre,
        apellido=user.perfil.apellido,
        email=user.correo,
        telefono=user.perfil.telefono,
        creado_en=user.creado_en
    )

@router.get("/User", response_model=list[UsuarioRead])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()

    result = []
    for u in users:
        # u.perfil es un objeto (1–1)
        result.append(UsuarioRead(
            id=u.id_usuario,
            nombre=u.perfil.nombre,
            apellido=u.perfil.apellido,
            email=u.correo,
            telefono=u.perfil.telefono,
            creado_en=u.creado_en
        ))
    return result

@router.put("/User/{usuario_id}", response_model=UsuarioRead)
def put_user(usuario_id: int, payload: UsuarioPut, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id_usuario == usuario_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    if not user.perfil:
        user.perfil = Perfil(
            id_usuario=user.id_usuario,
            nombre=payload.nombre,
            apellido=payload.apellido,
            telefono=payload.telefono
        )
    else:
        user.perfil.nombre = payload.nombre
        user.perfil.apellido = payload.apellido
        user.perfil.telefono = payload.telefono

    db.commit()
    db.refresh(user)

    # 4) Respuesta
    return UsuarioRead(
        id=user.id_usuario,
        nombre=user.perfil.nombre,
        apellido=user.perfil.apellido,
        email=user.correo,
        telefono=user.perfil.telefono,
        creado_en=user.creado_en
    )

@router.delete("/User/{usuario_id}")
def delete_user(usuario_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id_usuario == usuario_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(user)
    db.commit()
    return {"detail": "Usuario eliminado"}
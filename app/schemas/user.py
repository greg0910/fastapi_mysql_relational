from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import EmailStr
from datetime import datetime


class UsuarioCreate(SQLModel):
    email: EmailStr
    password: str = Field(min_length=3, max_length=72)
    nombre:Optional[str] = Field(default=None, min_length=3)
    apellido:Optional[str] = Field(default=None, min_length=3)
    telefono:Optional[str] = Field(default=None, min_length=10)

class UsuarioRead(SQLModel):
    id: int
    email: EmailStr
    nombre: str
    apellido: str
    telefono: str
    creado_en: datetime
    
class UsuarioPut(SQLModel):
    nombre:Optional[str] = Field(default=None, min_length=3)
    apellido:Optional[str] = Field(default=None, min_length=3)
    telefono:Optional[str] = Field(default=None, min_length=10)
    
class UsuarioPatch(SQLModel):
    email: Optional[EmailStr] = Field(default=None, min_length=3)
   
    
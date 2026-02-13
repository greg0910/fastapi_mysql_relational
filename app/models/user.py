from sqlalchemy import ForeignKey,String,DateTime
from sqlalchemy.orm import Mapped,mapped_column,relationship
from datetime import datetime
from ..db.db import Base


class User(Base):
    __tablename__ = "user_account"

    id_usuario: Mapped[int] = mapped_column(primary_key=True)
    correo: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    creado_en: Mapped[datetime] = mapped_column(DateTime,default=datetime.utcnow, nullable=False)

    perfil: Mapped["Perfil"] = relationship(back_populates="user", uselist=False,cascade= "all,delete-orphan")


class Perfil(Base):
    __tablename__ = "perfil"

    id_perfil: Mapped[int] = mapped_column(primary_key=True)
    id_usuario: Mapped[int] = mapped_column(ForeignKey("user_account.id_usuario"),nullable=False,unique=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    apellido: Mapped[str] = mapped_column(String(100), nullable=False)
    telefono: Mapped[str] = mapped_column(String(30), nullable=False)

    user: Mapped["User"] = relationship(back_populates="perfil")

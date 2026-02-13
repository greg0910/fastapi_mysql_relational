# 🔐 FastAPI + MySQL User Management API

API REST desarrollada con **FastAPI**, **SQLAlchemy** y **MySQL** para la gestión de usuarios, implementando un modelo relacional con buenas prácticas de arquitectura y seguridad.

El proyecto demuestra:

- Diseño de base de datos relacional con relación **1–1 (User ↔ Perfil)**
- Integridad referencial mediante **Foreign Keys**
- Restricción de **correo único**
- Hash seguro de contraseñas con **bcrypt**
- Manejo controlado de errores (409 Conflict)
- Separación clara entre **modelos ORM** y **schemas de validación**

---

## 🗄️ Modelo de Base de Datos

### user_account
- `id_usuario` (PK)
- `correo` (UNIQUE)
- `password` (hash bcrypt)
- `creado_en` (fecha de creación)

### perfil
- `id_perfil` (PK)
- `id_usuario` (FK UNIQUE → user_account.id_usuario)
- `nombre`
- `apellido`
- `telefono`

Cada usuario tiene un único perfil y cada perfil pertenece a un único usuario.

---

## 🔐 Seguridad

Las contraseñas no se almacenan en texto plano.  
Se aplica hash mediante bcrypt antes de persistir en la base de datos.

---

## 📌 Funcionalidades

- Crear usuario con perfil asociado
- Validación de correo único
- Listado de usuarios con datos relacionados
- Manejo adecuado de integridad y transacciones

---

## 🧠 Conceptos Aplicados

- ORM con SQLAlchemy
- Relaciones 1–1
- Integridad referencial
- Manejo de `IntegrityError`
- Arquitectura por capas
- Buenas prácticas de seguridad en APIs

---

Proyecto desarrollado como práctica avanzada de bases de datos relacionales con FastAPI.


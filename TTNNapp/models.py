
from datetime import datetime

from sqlalchemy import BigInteger, Date, DateTime, ForeignKey, String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .extensions import db


class Role(db.Model):
    __tablename__ = "roles"

    role_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    role_code: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    role_name: Mapped[str] = mapped_column(String(100), nullable=False)

    users: Mapped[list["User"]] = relationship(back_populates="role")


class User(db.Model):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.role_id"), nullable=False)
    full_name: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    phone: Mapped[str | None] = mapped_column(String(20))
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    account_status: Mapped[str] = mapped_column(String(20), nullable=False, default="ACTIVE")
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False)

    role: Mapped[Role] = relationship(back_populates="users")


class Student(db.Model):
    __tablename__ = "students"
    student_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), unique=True, nullable=False)
    student_code: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    date_of_birth: Mapped[object | None] = mapped_column(Date)


class Teacher(db.Model):
    __tablename__ = "teachers"
    teacher_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), unique=True, nullable=False)
    teacher_code: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    specialization: Mapped[str | None] = mapped_column(String(150))


class Employee(db.Model):
    __tablename__ = "employees"
    employee_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), unique=True, nullable=False)
    employee_code: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    position: Mapped[str | None] = mapped_column(String(100))

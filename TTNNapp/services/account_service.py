"""Nghiệp vụ tạo tài khoản và hồ sơ theo vai trò."""
from werkzeug.security import generate_password_hash
from ..extensions import db
from ..models import Employee, Role, Student, Teacher, User

PROFILE_MODELS = {"STUDENT": (Student, "student_code"), "TEACHER": (Teacher, "teacher_code"), "STAFF": (Employee, "employee_code")}

def create_account(full_name, email, password, role_code, profile_code=None):
    email = email.strip().lower()
    if not email.endswith("@gmail.com"): raise ValueError("Email phải có đuôi @gmail.com.")
    if User.query.filter_by(email=email).first(): raise ValueError("Email này đã tồn tại.")
    role = Role.query.filter_by(role_code=role_code).first()
    if role is None: raise ValueError("Vai trò không hợp lệ.")
    profile = PROFILE_MODELS.get(role_code)
    if profile and role_code != "STUDENT" and not profile_code: raise ValueError("Cần nhập mã giáo viên hoặc nhân viên.")
    user = User(full_name=full_name.strip(), email=email, role_id=role.role_id, password_hash=generate_password_hash(password), account_status="ACTIVE")
    db.session.add(user); db.session.flush()
    if profile:
        model, code_field = profile
        if role_code == "STUDENT":
            student = Student(user_id=user.user_id, student_code=f"TEMP{user.user_id}")
            db.session.add(student)
            db.session.flush()
            student.student_code = f"HV{student.student_id:06d}"
        elif model.query.filter(getattr(model, code_field) == profile_code.strip()).first():
            db.session.rollback(); raise ValueError("Mã hồ sơ này đã tồn tại.")
        else:
            db.session.add(model(user_id=user.user_id, **{code_field: profile_code.strip()}))
    db.session.commit()
    return user


def register_student(full_name, email, password):
    return create_account(full_name, email, password, "STUDENT")

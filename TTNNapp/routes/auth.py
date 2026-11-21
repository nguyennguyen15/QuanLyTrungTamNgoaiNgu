from flask import Blueprint, flash, render_template, request, session, redirect, url_for
from werkzeug.security import check_password_hash
from ..extensions import db
from ..models import User
from ..services.account_service import register_student
bp = Blueprint("auth", __name__)

@bp.get("/")
def index():
    return render_template("index.html")

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].strip().lower()
        user = db.session.execute(db.select(User).where(User.email == email)).scalar_one_or_none()
        if user is None or user.account_status != "ACTIVE" or not check_password_hash(user.password_hash, request.form["password"]):
            flash("Email hoặc mật khẩu không đúng.", "danger")
            return render_template("auth/login.html")
        session.clear()
        session["user_id"] = user.user_id
        session["role"] = user.role.role_code
        destinations = {
            "STUDENT": "student.courses", "TEACHER": "teacher.classes",
            "STAFF": "employee.invoices", "ADMIN": "admin.regulations",
        }
        return redirect(url_for(destinations[user.role.role_code]))
    return render_template("auth/login.html")

@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        password = request.form["password"]
        if password != request.form["confirm_password"]:
            flash("Mật khẩu xác nhận không khớp.", "danger")
            return render_template("auth/register.html")
        try:
            register_student(
                request.form["full_name"], request.form["email"], password,
            )
            flash("Đăng ký thành công. Hãy đăng nhập để tiếp tục.", "success")
            return redirect(url_for("auth.login"))
        except ValueError as error:
            flash(str(error), "danger")
    return render_template("auth/register.html")

@bp.get("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.index"))

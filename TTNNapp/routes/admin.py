from flask import Blueprint, flash, redirect, render_template, request, url_for
from ..decorators import role_required
from ..models import Role, User
from ..services.account_service import create_account
bp = Blueprint("admin", __name__, url_prefix="/admin")
@bp.get("/regulations")
@role_required("ADMIN")
def regulations():
    return render_template("admin/regulations.html")

@bp.route("/users", methods=["GET", "POST"])
@role_required("ADMIN")
def users():
    if request.method == "POST":
        try:
            create_account(request.form["full_name"], request.form["email"], request.form["password"], request.form["role_code"], request.form.get("profile_code"))
            flash("Đã lưu tài khoản vào MySQL.", "success")
        except ValueError as error:
            flash(str(error), "danger")
        return redirect(url_for("admin.users"))
    return render_template("admin/users.html", users=User.query.order_by(User.user_id.desc()).all(), roles=Role.query.order_by(Role.role_id).all())

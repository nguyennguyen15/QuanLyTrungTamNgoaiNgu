from flask import Blueprint, render_template
from flask import session
from ..decorators import role_required
from ..models import Student, User
bp = Blueprint("student", __name__, url_prefix="/student")
@bp.get("/courses")
@role_required("STUDENT")
def courses():
    return render_template("student/courses.html")

@bp.get("/profile")
@role_required("STUDENT")
def profile():
    user = User.query.get_or_404(session["user_id"])
    student = Student.query.filter_by(user_id=user.user_id).first_or_404()
    return render_template("student/profile.html", user=user, student=student)

from flask import Blueprint, render_template
from ..decorators import role_required
bp = Blueprint("teacher", __name__, url_prefix="/teacher")
@bp.get("/classes")
@role_required("TEACHER")
def classes():
    return render_template("teacher/classes.html")

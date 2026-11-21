from flask import Blueprint, render_template
bp = Blueprint("report", __name__, url_prefix="/reports")
@bp.get("/")
def dashboard():
    return render_template("reports/dashboard.html")

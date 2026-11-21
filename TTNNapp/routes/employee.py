from flask import Blueprint, render_template
from ..decorators import role_required

bp = Blueprint("employee", __name__, url_prefix="/employee")


@bp.get("/invoices")
@role_required("STAFF")
def invoices():
    return render_template("employee/invoices.html")

from sqlalchemy import text
from ..extensions import db


def class_has_space(class_id):
    row = db.session.execute(text(
        "SELECT c.max_students, COUNT(e.id) AS current_students FROM classes c "
        "LEFT JOIN enrollments e ON e.class_id = c.class_id AND e.enrollment_status IN ('CONFIRMED', 'STUDYING') "
        "WHERE c.class_id = :class_id GROUP BY c.class_id"), {"class_id": class_id}).mappings().first()
    return row is not None and row["current_students"] < row["max_students"]

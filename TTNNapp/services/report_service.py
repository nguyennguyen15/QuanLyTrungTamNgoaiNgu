from sqlalchemy import text
from ..extensions import db


def student_count_by_course():
    return db.session.execute(text(
        "SELECT co.course_name AS name, COUNT(e.enrollment_id) AS total FROM courses co "
        "LEFT JOIN classes cl ON cl.course_id = co.course_id "
        "LEFT JOIN enrollments e ON e.class_id = cl.class_id GROUP BY co.course_id"
    )).mappings().all()

from sqlalchemy import text

from ..extensions import db


def mark_invoice_paid(invoice_id):
    db.session.execute(
        text("UPDATE invoices SET invoice_status = 'PAID' WHERE invoice_id = :invoice_id"),
        {"invoice_id": invoice_id},
    )
    db.session.commit()

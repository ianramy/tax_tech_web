from . import db

class TaxData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    income = db.Column(db.Float, nullable=False)
    tax_rate = db.Column(db.Float, nullable=False)
    tax_amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<TaxData {self.id}>'

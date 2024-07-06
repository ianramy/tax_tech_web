from .models import TaxData
from . import db
from pydantic import BaseModel, ValidationError

class TaxDataInput(BaseModel):
    income: float
    tax_rate: float

def calculate_tax(income, tax_rate):
    return income * tax_rate

def add_tax_record(income, tax_rate):
    tax_amount = calculate_tax(income, tax_rate)
    new_record = TaxData(income=income, tax_rate=tax_rate, tax_amount=tax_amount)
    db.session.add(new_record)
    db.session.commit()
    return new_record

def validate_input(data):
    try:
        validated_data = TaxDataInput(**data)
        return validated_data
    except ValidationError as e:
        return str(e)

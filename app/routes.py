from flask import render_template, request, redirect, url_for, flash
from .models import TaxData
from .services import add_tax_record, validate_input
from . import db, current_app as app

@app.route('/')
def index():
    records = TaxData.query.all()
    return render_template('index.html', records=records)

@app.route('/add', methods=['GET', 'POST'])
def add_tax():
    if request.method == 'POST':
        data = request.form.to_dict()
        validation_error = validate_input(data)
        if validation_error:
            flash(f'Error: {validation_error}', 'danger')
            return redirect(url_for('add_tax'))

        income = float(data['income'])
        tax_rate = float(data['tax_rate'])
        add_tax_record(income, tax_rate)
        flash('Tax record added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add.html')

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from models import Product, db

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/moderate')
@login_required
def moderate():
    products = Product.query.all()
    return render_template('moderate.html', products=products)

@admin_bp.route('/delete_product/<int:product_id>')
@login_required
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        flash('Product deleted successfully!')
    return redirect(url_for('admin.moderate'))

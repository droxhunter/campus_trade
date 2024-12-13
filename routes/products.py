from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import Product, db

product_bp = Blueprint('products', __name__)

@product_bp.route('/list', methods=['GET', 'POST'])
@login_required
def list_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        quality = request.form['quality']
        image = request.files['image']
        
        image_path = f"static/uploads/{image.filename}"
        image.save(image_path)
        
        product = Product(name=name, description=description, price=price, quality=quality, seller_id=current_user.id, image_path=image_path)
        db.session.add(product)
        db.session.commit()
        
        flash('Product listed successfully!')
        return redirect(url_for('products.browse'))
    return render_template('list_product.html')

@product_bp.route('/browse')
def browse():
    products = Product.query.all()
    return render_template('browse.html', products=products)

@product_bp.route('/feedback/<int:product_id>', methods=['GET', 'POST'])
@login_required
def feedback(product_id):
    if request.method == 'POST':
        rating = request.form['rating']
        comment = request.form['comment']
        
        feedback = Feedback(product_id=product_id, user_id=current_user.id, rating=rating, comment=comment)
        db.session.add(feedback)
        db.session.commit()
        
        flash('Feedback submitted successfully!')
        return redirect(url_for('products.browse'))
    return render_template('feedback.html', product_id=product_id)

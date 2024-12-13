from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from models import Product, Feedback, db

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile')
@login_required
def profile():
    user_products = Product.query.filter_by(seller_id=current_user.id).all()
    feedbacks = Feedback.query.filter_by(user_id=current_user.id).all()
    return render_template('profile.html', user=current_user, products=user_products, feedbacks=feedbacks)

@user_bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        current_user.username = request.form['username']
        current_user.school = request.form['school']
        db.session.commit()
        flash('Profile updated successfully!')
        return redirect(url_for('user.profile'))
    return render_template('edit_profile.html', user=current_user)

@user_bp.route('/delete_account', methods=['POST'])
@login_required
def delete_account():
    db.session.delete(current_user)
    db.session.commit()
    flash('Account deleted successfully!')
    return redirect(url_for('auth.register'))

from flask import Blueprint, jsonify, request
import wechatpy

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/pay', methods=['POST'])
def pay():
    amount = request.json['amount']
    order_id = request.json['order_id']
    # Simulate payment logic or integrate with WeChat Pay API
    return jsonify({'status': 'Payment successful!', 'order_id': order_id})

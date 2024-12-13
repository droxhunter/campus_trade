from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from models import Message, db

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/send_message', methods=['POST'])
@login_required
def send_message():
    receiver_id = request.json['receiver_id']
    content = request.json['content']
    
    message = Message(sender_id=current_user.id, receiver_id=receiver_id, content=content)
    db.session.add(message)
    db.session.commit()
    return jsonify({'status': 'Message sent successfully!'})

@chat_bp.route('/get_messages/<int:user_id>', methods=['GET'])
@login_required
def get_messages(user_id):
    messages = Message.query.filter((Message.sender_id == current_user.id) & (Message.receiver_id == user_id) |
                                    (Message.sender_id == user_id) & (Message.receiver_id == current_user.id)).all()
    return jsonify([{'sender_id': m.sender_id, 'content': m.content, 'timestamp': m.timestamp} for m in messages])

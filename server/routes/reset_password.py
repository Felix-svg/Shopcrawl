from flask import request, jsonify
from utils.reset_email import send_reset_email
from config import app, bcrypt, db
from flask_jwt_extended import decode_token
from models.user import User

@app.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.json
    email = data.get('email')
    user = User.query.filter_by(email=email).first()

    if user:
        send_reset_email(user)
        return jsonify({'message': 'Password reset email sent'}), 200
    return jsonify({'message': 'Email not found'}), 404

@app.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    data = request.get_json()
    new_password = data.get('password')

    if not new_password:
        return jsonify({"error": "New password is required"}), 400
    
    try:
        decoded_token = decode_token(token)

        user_id = decoded_token.get('sub')  # Use 'sub' to extract user_id
        if not user_id:
            return jsonify({"error": "Invalid token structure"}), 400

        user = User.query.get(user_id)
        if user is None:
            return jsonify({"error": "Invalid token"}), 400
        
        user.password = bcrypt.generate_password_hash(new_password).decode('utf-8')
        db.session.commit()
        
        return jsonify({"message": "Password reset successful"}), 200
    except Exception as e:
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500
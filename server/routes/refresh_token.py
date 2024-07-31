from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from config import app
from datetime import timedelta

@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    """
    This endpoint allows users to refresh their access token using a valid refresh token.
    ---
    tags:
        - Auth
    summary: Token refresh
    description: Returns a new JWT access token using the refresh token.
    responses:
        200:
            description: Token refresh successful
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            access_token:
                                type: string
                                description: The new JWT access token.
                                example: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
        401:
            description: Invalid or expired refresh token
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            error:
                                type: string
                                example: "Invalid or expired refresh token"
    """
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity, expires_delta=timedelta(minutes=60))
    return jsonify({'access_token': access_token})
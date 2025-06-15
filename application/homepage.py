from flask import Blueprint, render_template, request, jsonify
import db

bp = Blueprint('homepage', __name__, url_prefix='/')


@bp.route("/")
def home():
    return render_template("index.html")


@bp.route("/add_crypto", methods=["POST"])
def add_crypto():
    try:
        user_id = request.json.get("user_id")
        crypto_name = request.json.get("crypto_name")
        crypto_symbol = request.json.get("crypto_symbol")
    except TypeError:
        return jsonify({"error": "Invalid input"})

    database = db.get_database()

    if not database:
        return jsonify({"error": "Database connection failed"})
    
    database.execute(
        "INSERT INTO crypto (user_id, crypto_name, crypto_symbol) VALUES (?, ?, ?)",
        (user_id, crypto_name, crypto_symbol)
    )

    database.commit()

    return jsonify({"message": "Crypto added successfully"})

from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for

from application import db

bp = Blueprint('homepage', __name__, url_prefix='/')


@bp.route("/")
def home():
    user = session.get("user_id")

    if not user:
        return redirect(url_for("auth.login"))

    database = db.get_db()

    try:
        cursor = database.execute(
            "SELECT crypto_name, crypto_symbol FROM crypto WHERE user_id = ?",
            (user,)
        )
        rows = cursor.fetchall()

        crypto_list = [
            {"crypto_name": row["crypto_name"], "crypto_symbol": row["crypto_symbol"]}
            for row in rows
        ]

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return render_template("index.html", crypto_list=crypto_list)


@bp.route("/add_crypto", methods=["POST"])
def add_crypto():
    database = db.get_db()

    if not database:
        return jsonify({"error": "Database connection failed"})

    try:
        user_id = request.json.get("user_id")
        crypto_name = request.json.get("crypto_name")
        crypto_symbol = request.json.get("crypto_symbol")
    except TypeError:
        return jsonify({"error": "Invalid input"})
    
    database.execute(
        "INSERT INTO crypto (user_id, crypto_name, crypto_symbol) VALUES (?, ?, ?)",
        (user_id, crypto_name, crypto_symbol)
    )

    database.commit()
    database.close()

    return jsonify({"message": "Crypto added successfully"})


@bp.route("/delete_crypto", methods=["POST"])
def delete_crypto():
    database = db.get_db()

    if not database:
        return jsonify({"error": "Database connection failed"})

    try:
        user_id = request.json.get("user_id")
        crypto_name = request.json.get("crypto_name")
        crypto_symbol = request.json.get("crypto_symbol")
    except TypeError as e:
        return jsonify({"error": "Invalid input"})
        
    database.execute(
        "DELETE FROM crypto WHERE user_id = ? AND crypto_name = ? AND crypto_symbol = ?",
        (user_id, crypto_name, crypto_symbol)
    )

    database.commit()
    database.close()

    return jsonify({"message": "Crypto deleted successfully"})

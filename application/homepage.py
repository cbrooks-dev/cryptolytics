from flask import Blueprint, render_template

bp = Blueprint('homepage', __name__, url_prefix='/')


@bp.route("/")
def home():
    return render_template("index.html")
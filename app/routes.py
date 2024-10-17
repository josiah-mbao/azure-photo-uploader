from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Placeholder for actual logic to display Azure data
    return render_template('index.html')

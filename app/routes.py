from flask import Blueprint, render_template, redirect, url_for
import subprocess

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Placeholder for actual logic to display Azure data
    return render_template('index.html')

@main.route('/backup')
def backup():
    # Call your Python backup script (this is just an example)
    subprocess.run(['python3', 'photo_backups.py'])
    return redirect(url_for('main.index'))

import ctypes
import os
from flask import Flask, render_template

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

APP_PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(APP_PATH, 'templates')
STATIC_DIR = os.path.join(APP_PATH, 'static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(use_reloader=False, debug=True, host="0.0.0.0", port=80)
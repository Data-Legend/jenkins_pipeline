from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    return (
        f"<h1>Hello!</h1>"
        f"<p>Current date is: <strong>{current_date}</strong></p>"
        f"<p>Current time is: <strong>{current_time}</strong></p>"
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

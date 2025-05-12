from flask import Flask, render_template, request, jsonify
from db import init_db, insert_choice
from datetime import datetime

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    user_id = request.remote_addr  # IP로 간단히 식별
    choice = data['choice']
    today = datetime.now().strftime('%Y-%m-%d')

    success = insert_choice(user_id, choice)
    if not success:
        return jsonify({'status': 'already_chosen'})

    # 여기서는 간단히 "match" 상태만 리턴
    return jsonify({'status': 'waiting'})  # 예시용

if __name__ == '__main__':
    app.run(debug=True)

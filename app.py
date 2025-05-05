from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
choices = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    global choices
    data = request.get_json()
    choices.append(data['choice'])

    if len(choices) < 2:
        return jsonify({'status': 'waiting'})
    else:
        result = 'match' if choices[0] == 'O' and choices[1] == 'O' else 'no_match'
        choices = []  # 초기화
        return jsonify({'status': result})

if __name__ == '__main__':
    app.run(debug=True)

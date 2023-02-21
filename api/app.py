from flask import Flask, jsonify
from flask import request, json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return "Состояние туризма в г. Нижний Новгород на 1 полугодие 2021 года"

@app.route('/api/params', methods=['GET'])
def get_all_params():
    with open('result.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return jsonify(data)

@app.route('/api/params/<name>', methods=['GET'])
def get_param(name):
    with open('result.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return jsonify(data['parametres'][name])

@app.route('/api/params', methods=['POST'])
def post_params():
     new_data = {"visitors": [{"name": "Общее число посетителей", "count": 2511801}]}
     with open("result.json", "r+", encoding="utf8") as f:
         file_data = json.load(f)
         file_data["parametres"].update(new_data)
         f.seek(0)
         json.dump(file_data, f, ensure_ascii=False, indent=2)

     return jsonify(new_data)

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, request, jsonify

app = Flask(__name__)

# 간단한 데이터베이스 대신 사용할 변수
data = {}

@app.route('/get_data', methods=['GET'])
def get_data():
    key = request.args.get('key')
    if key in data:
        app.logger.info("GET request: key='%s', value='%s'", key, data[key])
        return data[key]
    else:
        app.logger.warning("GET request: key='%s' not found", key)
        return "Key not found", 404

@app.route('/set_data', methods=['POST'])
def set_data():
    req_data = request.get_json()
    key = req_data.get('key')
    value = req_data.get('value')
    data[key] = value
    app.logger.info("POST request: key='%s', value='%s' stored", key, value)
    return "Successfully stored {} : {}".format(key, value)

if __name__ == '__main__':
    app.run(debug=True)
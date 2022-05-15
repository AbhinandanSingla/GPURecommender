import json

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('./index.html')


@app.route('/gpu', methods=['POST'])
def titanic():
    res = request.values.to_dict()
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)

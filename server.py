from flask import Flask, jsonify,request,session

app = Flask(__name__)


@app.route('/')
def index():
    response = jsonify({'value': True})  # Cambia el valor booleano según tus necesidades

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/search', methods=['GET'])
def search():
    args = request.args
    name = args.get('name')
    with open('var_virtual.txt','w') as f:
        f.write('{}'.format(name))
    response = jsonify({'name': name})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/validation')
def validation():
    with open('var_virtual.txt') as f:
        lines = f.readlines()
        print(lines)
    response = jsonify({'value': lines[0]})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.run(debug=True,host="10.20.131.251")

from flask import Flask,render_template,jsonify,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/profile")
def profilePage():
    return render_template('profile.html')

@app.route('/api/hello', methods=['GET'])
def helloMSG():
    name = request.args.get('name', 'Guest1')
    return jsonify({'message': 'Hello, this is a REST API!','status':200,'name':name})


if __name__ == '__main__':
    app.run(debug=True)
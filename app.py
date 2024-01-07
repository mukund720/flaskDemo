from flask import Flask,render_template,jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html',title="Home",description="hello how r u")

@app.route('/profile')
def hello_profile():
    return render_template('profile.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello, World!',"status":"200"}
    return jsonify(data)

@app.route('/api/data1', methods=['GET'])
def create_data():
    # Assuming incoming data is in JSON format
    data = request.args.get("name","Mukund")

    # Process the data (e.g., save to a database)
    # For simplicity, we'll just echo the received data
    return jsonify({"name":data})

if __name__ == '__main__':
    app.run(debug=True)

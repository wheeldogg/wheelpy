from flask import Flask
app = Flask(__name__)

app.config.update(dict(DEBUG=True))

# Say hello
@app.route('/')
def hello_world():
    return 'Welcome to json!'


#------------------------------ Actual API Starts here --------------------
@app.route('/api/getRandom/<int:p_1>', methods=['GET'])
def get_random(p_1):
    numbers = [random.randint(0, number) for number in xrange(0, p_1)]
    return make_response(jsonify({"numbers": numbers,
                    "numbersSum": sum(numbers)}), 200)

@app.route('/api/getRandom', methods=['GET'])
def getRandom():
    if not request.json or not "p_1" in request.json:
        abort(400)
        return
    numbers = [random.randint(0, number) for number in xrange(0, 
int(request.json['p_1']))]
    return make_response(jsonify({"numbers": numbers,
                    "numbersSum": sum(numbers)}), 200)



#------------------------------Error Handling------------------------------
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not Found"}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad Request"}), 400)

if __name__ == '__main__':
    app.run()

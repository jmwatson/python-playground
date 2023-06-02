from flask import Flask, request

app = Flask(__name__)

@app.route('/count', methods=['POST'])
def count_endpoint():
    # data = request.json
    word_to_count = request.args.get('word_to_count', '')
    delimiter = request.args.get('delimiter', '')

    if not word_to_count:
        return {'error': 'Invalid data provided'}, 400
    
    if not delimiter:
        return {'error': 'No delimiter provided'}, 400
    
    word_list = request.data.decode().split(delimiter)
    
    result = word_list.count(word_to_count)
    return {'count': result}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check_overlap', methods=['POST'])
def check_overlap():
    data = request.get_json()
    range1_start = data['range1']['start']
    range1_end = data['range1']['end']
    range2_start = data['range2']['start']
    range2_end = data['range2']['end']

    status= range1_start < range2_end and range1_end > range2_start
    
    response = {
        'overlap': status
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
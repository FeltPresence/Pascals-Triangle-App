""" This is where the main flask code should go """
from flask import Flask, request, jsonify
from generator.generator import Generator
import json

app = Flask(__name__)
gen = Generator()
def format_pascal_triangle(data):
    result = '{\n'
    for key, value in data.items():
        result += f'    "{key}": {value},\n'
    result = result[:-2] + '\n}'
    return result

@app.route('/pascal', methods=['GET', 'POST'])
def pascal():
    if request.method == 'POST':
        n = request.json['n']
        triangle = gen.generate(n)
        result = {}
        for i, row in enumerate(triangle):
            result[f'row_{i+1}'] = row
        formatted_result = format_pascal_triangle(result)
        return formatted_result
    else:
        return 'This endpoint only accepts POST requests.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

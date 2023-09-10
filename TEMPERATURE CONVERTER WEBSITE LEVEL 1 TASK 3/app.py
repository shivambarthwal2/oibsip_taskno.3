from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def convert_temperature(value, from_unit, to_unit):
    
    if from_unit == 'C':
        if to_unit == 'F':
            return (value * 9/5) + 32
        elif to_unit == 'K':
            return value + 273.15
    elif from_unit == 'F':
        if to_unit == 'C':
            return (value - 32) * 5/9
        elif to_unit == 'K':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'K':
        if to_unit == 'C':
            return value - 273.15
        elif to_unit == 'F':
            return (value - 273.15) * 9/5 + 32
    return value

@app.route('/', methods=['GET', 'POST'])
def index():
    converted_values = {'C': '', 'F': '', 'K': ''}
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            
            for to_unit in ['C', 'F', 'K']:
                converted_values[to_unit] = convert_temperature(value, from_unit, to_unit)
        except ValueError:
            error_message = "Invalid input. Please enter a valid number."
            return render_template('index.html', error_message=error_message)
    
    return render_template('index.html', converted_values=converted_values)

if __name__ == '__main__':
    app.run(debug=True)


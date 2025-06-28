
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        service = request.form.get('service')
        message = request.form.get('message')
        # In a real app, you'd save this to a database
        return jsonify({'status': 'success', 'message': 'Thank you! We\'ll contact you soon.'})
    return render_template('contact.html')

@app.route('/quote')
def quote():
    return render_template('quote.html')

@app.route('/api/calculate-quote', methods=['POST'])
def calculate_quote():
    data = request.json
    lawn_size = float(data.get('lawn_size', 0))
    service_type = data.get('service_type', 'basic')
    
    # Simple pricing calculation
    base_prices = {
        'basic': 25,
        'premium': 35,
        'deluxe': 45
    }
    
    base_price = base_prices.get(service_type, 25)
    total_price = base_price + (lawn_size * 0.5)
    
    return jsonify({
        'price': round(total_price, 2),
        'service': service_type.title(),
        'size': lawn_size
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

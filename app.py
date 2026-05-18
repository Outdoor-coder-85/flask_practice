from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Set your coding start date (Year, Month, Day)
    start_date = datetime(2026, 5, 1) 
    
    # Get today's exact date and calculate the difference
    today = datetime.now()
    difference = today - start_date
    days_coding = difference.days
    
    # Send the calculation directly to your home template
    return render_template('index.html', name="Ryan", days=days_coding)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # 1. Set your coding start date (Year, Month, Day)
    # Change these numbers to the day you actually started if you want!
    start_date = datetime(2026, 5, 1) 
    
    # 2. Get today's exact date
    today = datetime.now()
    
    # 3. Calculate the difference
    difference = today - start_date
    days_coding = difference.days
    
    # 4. Pass that "days_coding" variable into your HTML template!
    return render_template('index.html', days=days_coding)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
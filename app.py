from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Passing your practice string data directly into our HTML!
    user_name = "Ryan"  
    return render_template("index.html", name=user_name)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
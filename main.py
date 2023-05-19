from flask import Flask,request, render_template, redirect

app = Flask(__name__)

@app.route("/")
def get_all_posts():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/form_entry", methods=['GET','POST'])
def submit_data():
    name = request.form["name"]
    email = request.form["email"]
    phone_number = request.form["phone_number"]
    message = request.form["message"]

    print(name,email,phone_number,message)
    return "<h1>Successfully received your message</h1>"


if __name__=="__main__":
    app.run(debug=True)
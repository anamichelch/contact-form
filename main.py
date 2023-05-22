from flask import Flask,request, render_template, redirect

app = Flask(__name__)

@app.route("/")
def get_all_posts():
    return render_template("index.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone_number = request.form["phone_number"]
        message = request.form["message"]
        print(name, email, phone_number, message)
        return render_template("contact.html", message_sent=True)

    return render_template("contact.html",message_sent=False)



if __name__=="__main__":
    app.run(debug=True)
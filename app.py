from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
 
def homePage():
    return render_template("home.html")

@app.route("/result" , methods=["POST","GET"])

def resultPage():
    name=request.form.get("name")
    percentage=int(request.form.get("percentage"))
    course=request.form.get(("course"))
    return render_template("result.html", name=name, percentage=percentage, course=course)


if __name__ == ("__main__"):
    app.run(debug=True,port=8080)
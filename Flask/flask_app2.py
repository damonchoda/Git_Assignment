from flask import Flask, request, redirect, url_for, render_template_string
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://abir_mongodb:Abir12345@flaskassignment.fiis2h5.mongodb.net/?appName=FlaskAssignment")
db = client["testdb"]
collection = db["users"]

# Single HTML template (form + success message)
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Form Submission</title>
</head>
<body>

<h2>Submit Data</h2>

{% if success %}
    <h3 style="color:green;">Data submitted successfully</h3>
{% endif %}

<form method="POST">
    <input type="text" name="name" placeholder="Enter Name" required><br><br>
    <input type="email" name="email" placeholder="Enter Email" required><br><br>
    <button type="submit">Submit</button>
</form>

{% if error %}
    <p style="color:red;">{{ error }}</p>
{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        try:
            name = request.form.get("name")
            email = request.form.get("email")

            collection.insert_one({
                "name": name,
                "email": email
            })

            return redirect(url_for('success'))  # ✅ redirect here

        except Exception as e:
            return render_template_string(HTML_PAGE, error=str(e))

    return render_template_string(HTML_PAGE)
@app.route("/success")
def success():
    return """
    <h2>Data submitted successfully</h2>
    """
if __name__ == "__main__":
    app.run(debug=True)
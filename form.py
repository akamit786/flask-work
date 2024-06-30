from flask import Flask, render_template, request
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Process form data here
        # You can access form data using request.form['fieldname']
        # For example, if you have an input field with name 'name', you can access it using request.form['name']
        name = request.form['name']
        email = request.form['email']
        # Process the data further or store it in a database

        return f"Thank you, {name}! Your email ({email}) has been recorded."

    return render_template('form.html')

if __name__ == '__main__':
    app.run()
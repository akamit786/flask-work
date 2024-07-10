from flask import Flask, render_template
from flask import request
from flask import Flask
from flask import request
from flask import Flask, request
from flask import Flask, request

"""test Flask with this"""

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return f'''
    <section style="background-color: #f2f2f2; padding: 50px;">
        <h1>Welcome to My Flask App</h1>
        <p>This is the hero section of the page.</p>
        <p>Change the name in the <em >browser address bar</em> and reload the page.</p>
        <p><a href="/form">Go to Form d</a></p>
    </section>
    <h1>Hello, {name}!</h1>
    '''




@app.route('/form')
def form():
    return '''

    <form method="POST">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name"><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email"><br>
        <input type="submit" value="Submit">
    </form>
    
'''

if __name__ == '__main__':
    app.run(debug=True)
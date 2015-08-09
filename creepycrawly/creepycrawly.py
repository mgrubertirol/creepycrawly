from flask import Flask, render_template

# set the project root directory as the static folder, you can set others.
app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')
    #return 'Hello Lisi!'


if __name__ == '__main__':
    app.run(port=5000)

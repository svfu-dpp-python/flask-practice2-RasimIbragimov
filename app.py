from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    result = ""
    if 'expression' in request.args:
        print("================================================================================")
        print(request.args)
        print("================================================================================")
        app.logger.warning(request.args)
        print("================================================================================")
        result = str(eval(request.args['expression']))
    return render_template("index.html", result=result)

@app.route('/table/')
def table_page():
    return render_template('table.html')

@app.route('/result/<int:x>/<int:y>/')
def result_page(x, y):
    return render_template('result.html', x=x, y=y)
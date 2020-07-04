from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '5'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/99-bottles')
def index():
    count=[i for i in range(0,100)]
    count.reverse()
    return render_template(
        'bottles.html',
        title='Hello, World!',
        header='Welcome',
	count=count,
        sentecie="{} бутылок чего-то стояло на столе, одна упала и разбилась.",
        sentecie2="Нет больше бутылок на столе.",
        text='Jinja example'
     )


@app.route('/echo/')
def echo():
    print(request.path) # => '/echo/'
    print('request.data = ' + str(request.data))  
    return request.data


@app.route('/args/')
def args():
    arguments = {}  
    for key in request.args:
        arguments[key] = request.args.getlist(key)
    return render_template(
        'args.html',
	    arguments=arguments
     )


@app.route('/args-json/')
def argsjson():
    arguments = {}  
    for key in request.args:
        arguments[key] = request.args.getlist(key)
    return jsonify(arguments=arguments)
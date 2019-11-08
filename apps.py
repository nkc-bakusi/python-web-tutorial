from bottle import route, run, template

@route('/hello')
def hello():
    return "Hello Python!"

@route('/add')
def add():
  return template('add.html', title='Hello Python!!')

@route('/')
def index():
  return 'Hello index page!!'

run(host='localhost', port=8080, debug=True, reloader=True)
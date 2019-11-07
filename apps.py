from bottle import route, run, template

@route('/hello')
def hello():
    return "Hello Python!"

@route('/add')
def add():
  return template('add.html', title='Hello Python!!')

run(host='localhost', port=8080, debug=True)
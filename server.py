import bottle
import random

APP = bottle.default_app()

@APP.route('/')
def index():
  return '<p>Hello</p>'
  
@APP.route('/practice.html')
def practice():
  bottle.response.content_type = 'text/html'
  return bottle.static_file('index.html', '.')
   
  

if __name__ == '__main__':
  bottle.run(application=APP)

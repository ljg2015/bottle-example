import bottle
import random

APP = bottle.default_app()

@APP.route('/')
def index():
  return '<p>Hello</p>'
  
@APP.route('/practice.html')
def practice():
   
  

if __name__ == '__main__':
  bottle.run(application=APP)

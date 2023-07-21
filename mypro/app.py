#Writer Hello World
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"

if __name__ == '__main__':
   app.run()

#127.0.0.1:5000/hello/name
from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run(debug = True)

#127.0.0.1:5000/blog/11

from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

if __name__ == '__main__':
   app.run()

# /python/ > Hello Python
# /flask/ > 404 not found
from flask import Flask
app = Flask(__name__)

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

if __name__ == '__main__':
   app.run()


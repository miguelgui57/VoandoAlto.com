import os
from flask import Flask, render_template
from routes.web import web

app = Flask(__name__)
app.config['SECRET_KEY'] = '05c31152d33d28330bfd6cdfb5ee36e2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

@app.route('/')
def index():
  return render_template('index.html')



if __name__ == '__main__':
  port = int(os.environ.get("PORT", 5000))
  app.run(host = '0.0.0.0', port=port)
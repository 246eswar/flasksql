from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///mynotes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
class notes(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    desc=db.Column(db.String(200),nullable=False)
@app.route('/')
def home():
   note=notes(title="my first notes",desc="my description")
   
   return render_template('index.html')
@app.route('/about')
def about():
   return render_template('about.html')
@app.route('/contact')
def contact():
   return render_template('contact.html')
if __name__=='__main__':
    app.run()

from flask import Flask, render_template, url_for
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# db = SQLAlchemy(app)


# class Article(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(300), nullable=False)
#     intro = db.Column(db.String(300), nullable=False)
#     text = db.Column(db.Text, nullable=False)
#     date = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<Article %r>' % self.id
@app.route("/")
def index():
    return render_template("home.html")


@app.route("/about")
def about ():
     return render_template("about.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)





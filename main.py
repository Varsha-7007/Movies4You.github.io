from contextlib import _RedirectStream
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] =  'mysql+pymysql://root:@localhost/Movies'
db = SQLAlchemy(app)

class Booking_details(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    email=db.Column(db.String(20),nullable=False)
    phone=db.Column(db.String,nullable=False)
    date=db.Column(db.String,nullable=False)
    time=db.Column(db.String,nullable=False)
    no_of_tickets=db.Column(db.Integer,nullable=False)
    movie=db.Column(db.String(50), nullable=False)
    

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/booking", methods=['GET','POST'])
def booking():
    if(request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        date=request.form.get('date')
        time=request.form.get('time')
        no_of_tickets=request.form.get('no_of_tickets')
        movie=request.form.get('movie')

        entry=Booking_details(name=name,email=email,phone=phone,date=date,time=time,no_of_tickets=no_of_tickets,movie=movie)
        db.session.add(entry)
        db.session.commit()
        return render_template('seatbook.html')
    return render_template('booking.html')

@app.route("/seatbook")
def seatbook():
    return render_template('seatbook.html')


@app.route("/confirm")
def confirm():
    return render_template('confirm.html')




app.run(debug=True)

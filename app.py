from flask import Flask,request,render_template,request,jsonify,redirect,url_for
from model import Student,Session

from flask_sqlalchemy import SQLAlchemy,query

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///form.db'#it tekks the app which database you are using and wher it is located


db=SQLAlchemy(app)# it binds the app to the database


@app.route("/")
def show():
    return render_template("f.html")

@app.route("/dashboard",methods=["GET"])
def dashboard():
      return render_template("dashboard.html")

session=Session()
@app.route("/submit",methods=["POST"])
def submit_data():
    
        name=request.form.get("username")
       
        departement=request.form.get("depart")
        date=request.form.get("dates")
        status=request.form.get("statuses")
        roll_no=request.form.get("roll")

        student=Student(
              name=name,
              departement=departement,
              Date=date,
              status=status,
              roll=roll_no
        )
        session.add(student)
        session.commit()

      
        return render_template("f.html")


@app.route("/get",methods=["GET","POST"])
def get_student():
      students=session.query(Student).all()
      lst=[]

      for student in students:
            lst.append({
                  "name":student.name,
                  "status":student.status,
                  "departement":student.departement,
                  "date":student.Date,
                  "roll":student.roll
            })
            
 
      return jsonify(lst)      

     

        





if __name__=="__main__":
      app.run(debug=True)

import flask
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

email, pwd, fname, lname, country= None,None,None,None,None
phno=0
dbLoc='e:/CORP WORX/SANDBOX/project.db'
#def mail(x):
    #return 
def ip(x):
    return request.get_json()[x]
def message(x):
    if(x=='200'):
        return {"response-status-code":"200", "response-status-message":"successful"}
    elif(x=='400'):
        return {"response-status-code":"400", "response-status-message": "error bad data"}
    elif(x=='404'):
        return {"response-status-code":"404", "response-status-message":"not found"}
    else:
        return {"response-status-code":"500", "response-status-message":"internal server error"}
def disp(c):
        tot=[]
        all={}
        for row in c:
            all["email"]=row[0]
            all["pwd"]=row[1]
            all["fname"]=row[2]
            all["lname"]=row[3]
            all["phno"]=row[4]
            all["country"]=row[5]
            all["oname"]=row[6]
            all["omisn"]=row[7]
            all["sname"]=row[8]
            all["sdeg"]=row[9]
            all["syr"]=row[10]
            all["steam"]=row[11]
            all["mname"]=row[12]
            all["mdeg"]=row[13]
            all["myr"]=row[14]
            all["mteam"]=row[15]
            tot.append(all)  
        return tot  

@app.route("/create-account", methods=["POST"])
def create():
    if request.method=='POST':
        try:
            global email, pwd, fname, lname, country 
            global phno
            global ip
            conn = sqlite3.connect(dbLoc)
            email = ip('email')
            pwd = ip('pwd')
            fname = ip('fname')
            lname = ip('lname')
            phno = ip('phno')
            country = ip('country')
            if not(email and pwd and fname and lname and country and phno):
                return jsonify(message('400'))
            return jsonify(message('200'),{"":"goto: /student or /mentor or /org"})
            
        except:
            return jsonify(message('500'))
       
        finally:
            conn.close()
            
@app.route("/student", methods=["POST"])
def student():
    if request.method=='POST':
        try:
            conn = sqlite3.connect(dbLoc)
            sname = ip('sname')
            sdeg = ip('sdeg')
            syr = ip('syr')
            steam = ip('steam')
            conn.execute("INSERT INTO CORP (EMAIL, PWD, FNAME, LNAME, PHNO, COUNTRY, SNAME, SDEG, SYR, STEAM) \
                           VALUES (?,?,?,?,?,?,?,?,?,?)" ,(email, pwd, fname, lname, phno, country, sname, sdeg, syr, steam));
            conn.commit()
            return jsonify(message('200'))
        except:
            return jsonify(message('500'))
        finally:
            conn.close()
                   
@app.route("/mentor", methods=["POST"])
def mentor():
    if request.method=='POST':
        try:
            conn = sqlite3.connect(dbLoc)
            mname = ip('mname')
            mdeg = ip('mdeg')
            myr = ip('myr')
            mteam = ip('mteam')
            conn.execute("INSERT INTO CORP (EMAIL, PWD, FNAME, LNAME, PHNO, COUNTRY, MNAME, MDEG, MYR, MTEAM) \
                        VALUES (?,?,?,?,?,?,?,?,?,?)" ,(email, pwd, fname, lname, phno, country, mname, mdeg, myr, mteam));
            conn.commit()
            return jsonify(message('200'))
        except:
            return jsonify(message('500'))
        finally:
            conn.close()

@app.route("/org", methods=["POST"])
def org():
    if request.method=='POST':
        try:
            conn = sqlite3.connect(dbLoc)
            ip = request.get_json()
            oname = ip['oname']
            ip = request.get_json()
            omisn = ip['omisn']
            conn.execute("INSERT INTO CORP (EMAIL, PWD, FNAME, LNAME, PHNO, COUNTRY, ONAME, OMISN) \
                        VALUES (?,?,?,?,?,?,?,?)" ,(email, pwd, fname, lname, phno, country, oname, omisn));
            conn.commit()
            return jsonify(message('200'))
        except:
            return jsonify(message('500'))
        finally:
            conn.close()

@app.route("/all", methods=["GET"])
def all():
    if request.method=='GET':
        try:
            conn = sqlite3.connect(dbLoc)
            c = conn.execute("SELECT * from CORP").fetchall() 
            conn.commit()
            return jsonify(message('200'),{"":disp(c)})
        except:
            return jsonify(message('500'))
        finally:
            conn.close()

@app.route("/authenticate", methods=["POST"])
def authenticate():
    conn = sqlite3.connect(dbLoc)
    ip = request.get_json()
    email = ip['email']
    ip = request.get_json()
    pwd = ip['pwd']
    if not(ip and pwd):
         return jsonify(message('400'))
    c= conn.execute("SELECT * from CORP WHERE(EMAIL==? and PWD==?)",(email, pwd)).fetchall();
    if c:
        return jsonify(message('200'),{"":disp(c)})
    else:
        return jsonify(message('404'))

@app.route("/delete", methods=["POST"])
def delete():
    conn = sqlite3.connect(dbLoc)
    ip = request.get_json()
    email = ip['email']
    ip = request.get_json()
    pwd = ip['pwd']
    if not(email and pwd):
        return jsonify(message('400'))
    c= conn.execute("SELECT* from CORP where(EMAIL==? and PWD==?)",(email, pwd)).fetchone();
    conn.commit()
    if (c):
        conn.execute("DELETE from CORP where(EMAIL==? and PWD==?)",(email, pwd)).fetchone();
        return jsonify(message('200'))
    else:
        return jsonify(message('404'))

if __name__ =='__main__':
    app.run(debug=True,threaded=True)

import flask
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

email, pwd, fname, lname, country= None,None,None,None,None
phno=0

@app.route("/create-account", methods=["POST"])
def create():
    if request.method=='POST':
        try:
            global email, pwd, fname, lname, country 
            global phno
            conn = sqlite3.connect('e:/CORP WORX/SANDBOX/project.db')
            ip = request.get_json()
            email = ip['email']
            ip = request.get_json()
            pwd = ip['pwd']
            ip = request.get_json()
            fname = ip['fname']
            ip = request.get_json()
            lname = ip['lname']
            ip = request.get_json()
            phno = ip['phno']
            ip = request.get_json()
            country = ip['country']
            if not(email and pwd and fname and lname and country and phno):
                return jsonify({"response-status-code":"400", "response-status-message": "error no data"})
            return jsonify({"response-status-code":"200", "response-status-message":"successful", "":"goto:\n /student or /mentor or /org"})
            
        except:
            return jsonify({"response-status-code":"500", "response-status-message":"internal server error"})
       
        finally:
            conn.close()

@app.route("/student", methods=["POST"])
def student():
    if request.method=='POST':
        try:
            conn = sqlite3.connect('e:/CORP WORX/SANDBOX/project.db')
            ip = request.get_json()
            sname = ip['sname']
            ip = request.get_json()
            sdeg = ip['sdeg']
            ip = request.get_json()
            syr = ip['syr']
            ip = request.get_json()
            steam = ip['steam']

            conn.execute("INSERT INTO CORP (EMAIL, PWD, FNAME, LNAME, PHNO, COUNTRY, SNAME, SDEG, SYR, STEAM) \
                           VALUES (?,?,?,?,?,?,?,?,?,?)" ,(email, pwd, fname, lname, phno, country, sname, sdeg, syr, steam));
            conn.commit()
            return jsonify({"response-status-code":"200", "response-status-message":"rec added successfully"})
        except:
            return jsonify({"response-status-code":"500", "response-status-message":"internal server error"})
        finally:
            conn.close()

                    
@app.route("/mentor", methods=["POST"])
def mentor():
    if request.method=='POST':
        try:
            conn = sqlite3.connect('e:/CORP WORX/SANDBOX/project.db')
            ip = request.get_json()
            mname = ip['mname']
            ip = request.get_json()
            mdeg = ip['mdeg']
            ip = request.get_json()
            myr = ip['myr']
            ip = request.get_json()
            mteam = ip['mteam']
            conn.execute("INSERT INTO CORP (EMAIL, PWD, FNAME, LNAME, PHNO, COUNTRY, MNAME, MDEG, MYR, MTEAM) \
                        VALUES (?,?,?,?,?,?,?,?,?,?)" ,(email, pwd, fname, lname, phno, country, mname, mdeg, myr, mteam));
            conn.commit()
            return jsonify({"response-status-code":"200", "response-status-message":"rec added successfully"})
        except:
            return jsonify({"response-status-code":"500", "response-status-message":"internal server error"})
        finally:
            conn.close()

@app.route("/org", methods=["POST"])
def org():
    if request.method=='POST':
        try:
            conn = sqlite3.connect('e:/CORP WORX/SANDBOX/project.db')
            ip = request.get_json()
            oname = ip['oname']
            ip = request.get_json()
            omisn = ip['omisn']
            conn.execute("INSERT INTO CORP (EMAIL, PWD, FNAME, LNAME, PHNO, COUNTRY, ONAME, OMISN) \
                        VALUES (?,?,?,?,?,?,?,?)" ,(email, pwd, fname, lname, phno, country, oname, omisn));
            conn.commit()
            return jsonify({"response-status-code":"200", "response-status-message":"rec added successfully"})
        except:
            return jsonify({"response-status-code":"500", "response-status-message":"internal server error"})
        finally:
            conn.close()

@app.route("/all", methods=["GET"])
def all():
    if request.method=='GET':
        try:
            conn = sqlite3.connect('e:/CORP WORX/SANDBOX/project.db')
            c = conn.execute("SELECT * from CORP").fetchall()
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
            conn.commit()
            return jsonify({"response-status-code":"200", "response-status-message":"displayed successfully","":tot})
        except:
            return jsonify({"response-status-code":"500", "response-status-message":"internal server error"})
        finally:
            conn.close()

@app.route("/authenticate", methods=["POST"])
def authenticate():
    conn = sqlite3.connect('e:/CORP WORX/SANDBOX/project.db')
    ip = request.get_json()
    email = ip['email']
    ip = request.get_json()
    pwd = ip['pwd']
    if not(ip and pwd):
         return jsonify({"response-status-code":"400", "response-status-message":"invalid credentials"})
    c= conn.execute("SELECT * from CORP WHERE(EMAIL==? and PWD==?)",(email, pwd)).fetchone();
    if c:
        all={}
        all["email"]=c[0]
        all["pwd"]=c[1]
        all["fname"]=c[2]
        all["lname"]=c[3]
        all["phno"]=c[4]
        all["country"]=c[5]
        all["oname"]=c[6]
        all["omisn"]=c[7]
        all["sname"]=c[8]
        all["sdeg"]=c[9]
        all["syr"]=c[10]
        all["steam"]=c[11]
        all["mname"]=c[12]
        all["mdeg"]=c[13]
        all["myr"]=c[14]
        all["mteam"]=c[15]
        return jsonify({"response-status-code":"200", "response-status-message":"authenticated", "":all})
    else:
        return jsonify({"response-status-code":"404", "response-status-message":"account not found"})

@app.route("/delete", methods=["POST"])
def delete():
    conn = sqlite3.connect('e:/CORP WORX/SANDBOX/project.db')
    ip = request.get_json()
    email = ip['email']
    ip = request.get_json()
    pwd = ip['pwd']
    if not(email and pwd):
        return jsonify({"response-status-code":"400", "response-status-message":"invalid credentials"})
    c= conn.execute("SELECT* from CORP where(EMAIL==? and PWD==?)",(email, pwd)).fetchone();
    conn.commit()
    if (c):
        conn.execute("DELETE from CORP where(EMAIL==? and PWD==?)",(email, pwd)).fetchone();
        return jsonify({"response-status-code":"200", "response-status-message":"record deleted successfully"})
    else:
        return jsonify({"response-status-code":"404", "response-status-message":"account not found"})

if __name__ =='__main__':
    app.run(debug=True,threaded=True)

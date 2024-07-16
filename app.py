from flask import Flask, render_template,jsonify
from database import load_jobs_from_db

app = Flask(__name__)  ##when u run this u will get __main__ as name variable has main value for app.py


@app.route("/")
def hello_aps():
  jobs = load_jobs_from_db()
  return render_template("home.html",jobs=jobs,companys_name="APS Careers Website")
  
@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

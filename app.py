from flask import Flask, render_template, jsonify
from database import load_jobs_from_db
from sqlalchemy import text

app = Flask(__name__)

# JOBS = [
#   {
#     'id' : 1,
#     'title' : 'Python Developer',
#     'location' : 'New York',
#     'salary' : '100K'
#   },
# {
#     'id' : 2,
#     'title' : 'Data Analyst',
#     'location' : 'New York',
#     'salary' : '200K'
#   },
# {
#     'id' : 3,
#     'title' : 'Application Specialist',
#     'location' : 'Toronto',
#     'salary' : '80K'
#   },
# ]





@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html',jobs=jobs,company_name='Jovian')

@app.route("/api/jobs")

def list_jobs():
  return jsonify(jobs)

if __name__ == "__main__":
  print("I am inside the if now")
  app.run(host='0.0.0.0', debug=True)




# print("Hello")
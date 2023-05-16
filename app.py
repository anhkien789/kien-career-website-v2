from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengalury, India',
  'salary': '$1000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Delhi, India',
  'salary': '$1500'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'San Francisco, USA',
  'salary': '$3000'
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name="Kien")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

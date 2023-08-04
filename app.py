from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Clichy-Sous-Bois (93)',
        'salary': '40 000.00€',
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Aulnay-Sous-Bois (93)',
        'salary': '48 000.00€',
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Coubron (93)',
        'salary': '32 000.00€',
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Montfermeil (93)',
        'salary': '35 000.00€',
    },
]

@app.route("/")
def hello_world():
    return render_template('home.html', 
                           jobs=JOBS,
                           company_name='EkimCorp')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

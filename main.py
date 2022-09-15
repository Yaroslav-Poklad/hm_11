from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidate_by_name, get_candidate_by_skill

app = Flask(__name__)

@app.route("/")
def page_index():
    candidates = load_candidates_from_json()
    return render_template("list.html", candidates=candidates)



app.run()
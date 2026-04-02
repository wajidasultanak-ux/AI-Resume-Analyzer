from flask import Flask, render_template, request
import PyPDF2
from skills import find_skills

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():

    file = request.files['resume']
    reader = PyPDF2.PdfReader(file)

    text = ""
    for page in reader.pages:
        text += page.extract_text()

    skills = find_skills(text)

    jobs = []

    if "python" in skills:
        jobs.append("Python Developer")

    if "java" in skills:
        jobs.append("Java Developer")

    if "html" in skills or "css" in skills:
        jobs.append("Frontend Developer")

    if "machine learning" in skills:
        jobs.append("ML Engineer")

    # Resume Score
    score = 0
    
    # Skill based score
    if len(skills) >= 5:
        score += 40
        
    elif len(skills) >= 3:
        score += 25
    else:
        score += 10
        
    # Project detection
    if "project" in text.lower():
        score += 20
        
    # Education detection
    text_lower = text.lower()
    if ("btech" in text_lower or 
        "b.tech" in text_lower or
        "b tech" in text_lower or
        "mtech" in text_lower or
        "m.tech" in text_lower or
        "m tech" in text_lower or
        "bachelor of technology" in text_lower or
        "master of technology" in text_lower):
        score += 10

    # Experience detection
    if "experience" in text.lower():
        score += 20

    # Base formatting score
        score += 10

    return render_template("index.html", skills=skills, jobs=jobs, score=score)

if __name__ == "__main__":
    app.run(debug=True)

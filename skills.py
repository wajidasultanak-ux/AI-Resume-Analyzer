skill_set = [
"python",
"java",
"html",
"css",
"javascript",
"machine learning",
"sql",
"data analysis",
"flask"
]

def find_skills(text):

    detected = []

    for skill in skill_set:

        if skill.lower() in text.lower():
            detected.append(skill)

    return detected

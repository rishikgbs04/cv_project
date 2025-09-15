from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.shortcuts import render

def cv_view(request):
    context = {
        "name": "Rishik Gannavarapu",
        "title": "Software Engineer",
        "email": "rishikgbs04@gmail.com",
        "phone": "480-999-8941",
        "location": "Brooklyn, NY",
        "linkedin": "https://www.linkedin.com/in/rishik-gannavarapu",
        "github": "https://github.com/rishikgbs04",

        "summary": "Dynamic and detail-oriented Software Engineer with a strong skill set in frontend and backend development. Specialized in full-stack applications with React.js, Node.js, Firebase, and PostgreSQL. Experienced in Agile teams, delivering scalable and production-ready features.",

        "skills": [
            "Python", "JavaScript", "TypeScript", "HTML", "CSS", "SQL",
            "React.js", "Node.js", "Firebase", "Tailwind CSS", "PostgreSQL",
            "Git", "Figma", "Agile/Scrum", "REST APIs", "Google Cloud", "Testing"
        ],

        "education": [
            {"degree": "MS in Computer Science", "school": "New York University", "year": "Expected 2026"},
            {"degree": "BS in Computer Science", "school": "Arizona State University", "year": "2025", "gpa": "3.95"},
        ],

        "experience": [
            {"role": "Frontend Developer", "company": "Qualaces Inc.", "years": "Aug 2024 – May 2025", "details": [
                "Contributed to no-code AI-based test automation tool",
                "Built frontend components using React.js and Tailwind CSS",
                "Collaborated with CEO/CTO for feedback and product alignment",
                "Practiced Agile methodologies"
            ]},
            {"role": "UGTA (Software Engineering)", "company": "ASU CSE 360", "years": "Jan 2024 – Dec 2024", "details": [
                "Guided 100+ students in Agile methodology and software engineering practices",
                "Created study materials and led weekly sessions",
                "Assisted in course syllabus design"
            ]},
            {"role": "Software Engineer Intern", "company": "UpSquad", "years": "May 2024 – Aug 2024", "details": [
                "Developed front-end features with React.js and Tailwind CSS",
                "Collaborated with cross-functional teams",
                "Participated in code reviews and Agile ceremonies"
            ]},
        ],

        "projects": [
            {"name": "Qualaces AI Test Tool", "desc": "Codeless testing tool using AI + image recognition, with React/Tailwind frontend and Firebase integration."},
            {"name": "Visualize COVID-19 Data", "desc": "Dashboard web app fetching and visualizing real-time COVID-19 data with filters and responsive design."},
            {"name": "SkillBridge", "desc": "Entrepreneurship platform connecting learners with micro-internships. Designed UI/UX and built MVP in React."},
        ],

        "extras": [
            "National Rifle Shooter representing India",
            "Volunteer mentor for coding workshops at ASU"
        ]
    }
    return render(request, "resume/cv.html", context)

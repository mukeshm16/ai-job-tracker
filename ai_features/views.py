from django.shortcuts import render

# Create your views here.

def interview_questions(request):

    questions = []

    if request.method == "POST":

        role = request.POST.get('role')

        if "python" in role.lower():

            questions = [

                "Explain OOP concepts in Python",

                "What is list comprehension?",

                "Difference between list and tuple?",

                "What is Django ORM?",

                "Explain decorators in Python"
            ]

        elif "web" in role.lower():

            questions = [

                "What is REST API?",

                "Difference between frontend and backend?",

                "Explain HTTP methods",

                "What is authentication?",

                "Explain MVC architecture"
            ]

        else:

            questions = [

                "Tell me about yourself",

                "What are your strengths?",

                "Why should we hire you?",

                "Explain your projects",

                "What are your career goals?"
            ]

    context = {
        'questions': questions
    }

    return render(request, 'interview_questions.html', context)
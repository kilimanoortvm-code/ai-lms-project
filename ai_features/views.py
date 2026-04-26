from django.http import JsonResponse

def ai_chat(request):
    message = request.GET.get('message', '').lower()


    if "hello" in message or "hi" in message:
        reply = "Hello! I am your AI Tutor. Ask me anything "

    elif "what is python" in message or "python" in message:
        reply = "Python is a programming language used for AI, web development, and more."

    elif "what is django" in message or "django" in message:
        reply = "Django is a Python framework used to build web applications quickly."

    elif "artificial intelligence" in message or "what is ai" in message:
        reply = "Artificial Intelligence helps machines think and learn like humans."

    elif "machine learning" in message:
        reply = "Machine Learning is a part of AI where systems learn from data."

    elif "html" in message:
        reply = "HTML is used to create the structure of web pages."

    elif "css" in message:
        reply = "CSS is used to style and design web pages."

    elif "javascript" in message:
        reply = "JavaScript makes web pages interactive."

    elif "database" in message:
        reply = "A database stores and manages data efficiently."

    elif "sql" in message:
        reply = "SQL is used to manage and query data in databases."

    elif "lms" in message:
        reply = "LMS stands for Learning Management System."

    elif "quiz" in message:
        reply = "A quiz is used to test knowledge through questions."

    elif "teacher" in message:
        reply = "A teacher manages courses, notes, and quizzes."

    elif "student" in message:
        reply = "A student learns courses, downloads notes, and attempts quizzes."

    elif "who developed python" in message:
        reply = "Python was developed by Guido van Rossum."
    
    else:
        reply = "AI Tutor: I am still learning. Please ask about Python, Django, AI, LMS, HTML, CSS, database, quiz, teacher, or student."
    

    return JsonResponse({"reply": reply})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks
from django.views.decorators.csrf import csrf_exempt  # To prevent CSRF issues (not recommended for production)

def homePage(request):
    tasks = Tasks.objects.all()  # Fetch all tasks
    return render(request, 'homePage.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")  # Get form data
        content = request.POST.get("content")

        if title and content:
            Tasks.objects.create(title=title, content=content)  # Save to DB

        return redirect("home")  # Redirect to home page
    
    return redirect("home")  # If GET request, do nothing

def delete_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    task.delete()
    return redirect("home")

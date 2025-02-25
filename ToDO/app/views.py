from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks

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


def update_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)  # Get the task or return 404

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title and content:
            task.title = title
            task.content = content
            task.save()  # Save the updated task

        return redirect("home")  # Redirect to home page

    return redirect("home")





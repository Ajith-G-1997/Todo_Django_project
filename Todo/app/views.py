from django.shortcuts import render,redirect
from .models import Task
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

# Create your views here.
def index(request):
    task = Task.objects.filter(is_completed=False)
    completed = Task.objects.filter(is_completed=True)
    context = {
        'task':task,
        'completed':completed
    }
    return render(request,'index.html',context)


def add_task(request):
    if request.method=='POST':
        task=request.POST.get('task')
        Todo=Task.objects.create(task=task)
        Todo.save()
        return redirect('index')
    



def mark_as_done(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = True 
    task.save()
    return redirect('index')  

def mark_as_undone(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = False  
    task.save()
    return redirect('index') 


def update_task(request, update_id):
    # Get the task object or return a 404 if not found
    get_task = get_object_or_404(Task, id=update_id)
    
    if request.method == 'POST':
        # Get the new task name from the POST request
        new_task = request.POST.get('task')
        
        # Update and save the task
        if new_task:
            get_task.task = new_task
            get_task.save()
            return redirect('index')  # Redirect to the desired URL name or view
        else:
            # Handle the case where 'task' is empty or None
            context = {
                'task': get_task,
                'error': 'Task name cannot be empty'
            }
            return render(request, 'update.html', context)
    else:
        # Render the update template with the task context
        context = {
            'get_task': get_task
        }
        return render(request, 'update.html', context)

def delete_task(request, task_id):
    # Ensure that the request is a POST request
    if request.method == 'POST':
        # Retrieve the task using the ID, or raise a 404 error if not found
        task = get_object_or_404(Task, id=task_id)
        # Delete the task from the database
        task.delete()
        # Add a success message
        messages.success(request, 'Task successfully deleted!')
    # Redirect to the task list page after deletion
    return redirect('index')  # Replace 'index' with your actual task list view name
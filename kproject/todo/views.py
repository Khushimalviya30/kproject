from django.shortcuts import render,redirect,get_object_or_404
from todo.forms import Todoform, contactform
from todo.models import Todo
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')

def contact(request):
    concheck = contactform(request.POST or None)
    if concheck.is_valid():
        concheck.save()
        return redirect("home")
    return render(request,'contact.html',{'cform':concheck})

def about(request):
    return render(request,'about.html')

@login_required
def service(request):
    return render(request,'courses.html')

@login_required
def addreviews(request):
    tf = Todoform(request.POST or None)
    if tf.is_valid():
        tf.save()
        return redirect("allreviews")

    return render(request,'addreviews.html',{'form':tf})

@login_required
def allreviews(request):
    allfeedback = Todo.objects.all() #reading the data from databse
    return render(request,'allreviews.html',{'todos':allfeedback})

@login_required
def todoedit(request,pk):
    todo=get_object_or_404(Todo,pk=pk)
    todoform=Todoform(request.POST or None,instance=todo)
    if todoform.is_valid():
        todoform.save()
        return redirect('allreviews')
    return render(request,'addreviews.html',{'form':todoform})

#deletion
@login_required
def tododelete(request,pk):
    todo = get_object_or_404(Todo,pk=pk)
    if request.method=='POST':
        todo.delete()
        return redirect('allreviews')
    return render(request,'tododelete.html',{'todo':todo})






from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm
from .models import Topic


# Create your views here.
def index(request):
    return render(request,'learning_logs/index.html')

def new_topic(request):
    if request.method != 'POST':
        form=TopicForm()
    else:
        form=TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic'))

    context={'form':form}

    return render(request,'learning_logs/new_topic.html',context)


from django.shortcuts import render

# Create your views here.

def form(request):
    return render(request, 'form.html')

def questionnaire(request):
    return render(request, 'questionnaire.html')

def graphs(request):
    return render(request, 'graphs.html')
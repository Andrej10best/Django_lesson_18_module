from django.shortcuts import render

# Create your views here.
def get_class(request):
    return render(request, 'class_template.html')

def get_func(request):
    return render(request, 'func_template.html')
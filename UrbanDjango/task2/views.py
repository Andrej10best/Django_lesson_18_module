from django.shortcuts import render

# Create your views here.
def get_class(request):
    return render(request, 'second_task\\class_template.html')

def get_func(request):
    return render(request, 'second_task\\func_template.html')
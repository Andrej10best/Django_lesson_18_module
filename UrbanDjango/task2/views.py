from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def get_func(request):
    return render(request, 'second_task\\func_template.html')

class GetClass(TemplateView):
    template_name = 'second_task\\class_template.html'
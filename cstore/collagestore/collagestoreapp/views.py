from django.shortcuts import render, redirect

from .form import OrderForm
from .models import Courses
from django.views.generic.edit import CreateView


# Create your views here.


def home1(request):
    return render(request, 'home1.html')

def contact(request):
    return render(request, 'contact.html')

def sucess(request):
    return render(request, 'sucess.html')


class place_order(CreateView):
    form_class = OrderForm
    template_name = 'order.html'


    def form_valid(self, form):
        form.save()
        return redirect('/sucess')


def get_courses(request):
    dept_id = request.GET.get('department')
    courses = Courses.objects.filter(course_dept=dept_id).order_by('course_name')
    return render(request, 'course_options.html', {'courses': courses})

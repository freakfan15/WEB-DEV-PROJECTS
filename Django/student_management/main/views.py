from django.db.models import fields
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from django.views.generic import(
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.edit import UpdateView

from main import models
# Create your views here.

class Index(View):
    def get(self, request):
        return HttpResponse('GET request')
    def post(self, request):
        return HttpResponse('POST request')

#this class maps the model class and the template to be rendered and shows the college details.
class CollegeDetail(DetailView):
    model = models.College
    template_name = 'main/college_detail.html'

class CollegeList(ListView):
    model = models.College
    template_name = 'main/college_list.html'
    context_object_name = 'colleges'

class CreateCollege(CreateView):
    model = models.College
    template_name = 'main/create_college.html'
    fields = '__all__' #THIS specifies what fields do we want django to create like UpdateTime, create time, delete time etc
    success_url ='/college'

class UpdateCollege(UpdateView):
    model = models.College
    template_name = 'main/create_college.html'
    fields = '__all__' #THIS specifies what fields do we want django to create like UpdateTime, create time, delete time etc
    success_url ='/college'

class CreateStudent(CreateView):
    model = models.Student
    template_name = 'main/create_student.html'
    fields = '__all__'
    success_url = '/'

class DeleteStudent(DeleteView):
    model = models.Student
    template_name = 'main/confirm.html'
    #we need to create a success url to redirect to after the confirmation page
    success_url = '/'





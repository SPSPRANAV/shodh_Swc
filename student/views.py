from django.shortcuts import render
from django.http import HttpResponse
from .models import Intern_Model
from .models import User_profile
from .models import Applyform
from django.views.generic import CreateView

# Create your views here.
user_name="SPS Pranav"
user_branch="CSE"
user_cpi=7.86
def profile(request):
    user_name="SPS Pranav"
    user_branch="CSE"
    user_cpi=7.86
    user_list = []
    user_list.extend((user_name,user_branch,user_cpi))
    context={'user_list': user_list ,}
    return render(request, 'student/profile.html',context)

def index(request):
    list = Intern_Model.objects.all()
    context = {'list': list ,}
    return render(request, 'student/index.html', context)
def apply(request):
        slist = Intern_Model.objects.filter(min_cpi__lte=user_cpi)
        context = {'slist': slist ,}
        return render(request, 'student/apply.html',context)
class ApplyCreateView(CreateView):
    model = Applyform
    fields = ('cv', 'bio')

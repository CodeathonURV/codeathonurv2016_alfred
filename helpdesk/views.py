from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import UpdateView
from django.db.models import Avg
from helpdesk.models import *
from helpdesk.tables import *

from .forms import *

# Create your views here.
@login_required
def pdi_topics(request):
    try:
        request.user.pdi
    except:
        return HttpResponse('Unauthorized', status=401)
    table = TopicsTable(Topic.objects.filter(author__id=request.user.id))
    # topic_author = Topic.objects.filter(author__id=request.user.id)
    # topic_receiver = Topic.objects.filter(receiver__id=request.user.id)
    return render(request,'helpdesk/topics.html', {'section': 'topics', 'rol' : 'pdi', 'table':table})

@login_required
def  pdi_new_topic_for_pas(request):
    #TODO
    None

@login_required
def pdi_ask_faq(request):
    try:
        request.user.pdi
    except:
        return HttpResponse('Unauthorized', status=401)
    return render(request,'helpdesk/ask_faq.html', {'section': 'ask_faq', 'rol' : 'pdi'})

@login_required
def pdi_ask(request):
    try:
        request.user.pdi
    except:
        return HttpResponse('Unauthorized', status=401)
    return render(request,'helpdesk/create_topic_for_pdi.html', {'section': 'ask', 'rol' : 'pdi'})

@login_required
def pdi_topic(request, topic_id):
    try:
        request.user.pdi
    except:
        return HttpResponse('Unauthorized', status=401)
    topic = Topic.objects.get(pk=topic_id)
    comments = list(Comment.objects.filter(topic__id=topic_id)).order_by('date_published')
    return render(request,'helpdesk/topic.html', {'section': 'topic', 'rol' : 'pdi', 'topic':topic, 'comments':comments})

@login_required
def pdi_ranking(request):
    try:
        request.user.pdi
    except:
        return HttpResponse('Unauthorized', status=401)
    pdi_users = Pdi.objects.all()
    user_ranking = {}
    for pdi_user in pdi_users:
        user_ranking[pdi_user] = Comment.objects.filter(author=pdi_user.user).aggregate(Avg("rating")).values()[0]

    return render(request,'helpdesk/ranking.html', {'section': 'ranking', 'rol' : 'pdi', 'user_ranking':user_ranking})

@login_required
def pdi_profile(request):
    try:
        request.user.pdi
    except:
        return HttpResponse('Unauthorized', status=401)
    return render(request,'helpdesk/pdi_profile.html', {'section': 'profile', 'rol' : 'pdi'})



@login_required
def pas_topics(request):
    try:
        request.user.pas
    except:
        return HttpResponse('Unauthorized', status=401)
    return render(request,'helpdesk/topics.html', {'section': 'topics', 'rol' : 'pas'})


@login_required
def  pas_new_topic_for_pas(request):
    #TODO
    None

@login_required
def pas_ask_faq(request):
    try:
        request.user.pas
    except:
        return HttpResponse('Unauthorized', status=401)
    return render(request,'helpdesk/ask_faq.html', {'section': 'ask_faq', 'rol' : 'pas'})

@login_required
def pas_ask(request):
    try:
        request.user.pas
    except:
        return HttpResponse('Unauthorized', status=401)
    return render(request,'helpdesk/create_topic_for_pdi.html', {'section': 'ask', 'rol' : 'pas'})

@login_required
def pas_topic(request):
    try:
        request.user.pas
    except:
        return HttpResponse('Unauthorized', status=401)
    topic = Topic.objects.get(pk=topic_id)
    comments = list(Comment.objects.filter(topic__id=topic_id)).order_by('date_published')
    return render(request,'helpdesk/topic.html', {'section': 'topic', 'rol' : 'pas', 'topic':topic, 'comments':comments})

@login_required
def pas_ranking(request):
    try:
        request.user.pas
    except:
        return HttpResponse('Unauthorized', status=401)
    pas_users = Pas.objects.all()
    user_ranking = {}
    for pas_user in pas_users:
        user_ranking[pas_user] = Comment.objects.filter(author=pas_user.user).aggregate(Avg("rating")).values()[0]
    print 'user_comments', user_comments
    return HttpResponse('Unauthorized', status=401)
    return render(request,'helpdesk/ranking.html', {'section': 'ranking', 'rol' : 'pas', 'user_ranking':user_ranking})

@login_required
def pas_profile(request):
    try:
        request.user.pas
    except:
        return HttpResponse('Unauthorized', status=401)
    return render(request,'helpdesk/pas_profile.html', {'section': 'profile', 'rol' : 'pas'})



@login_required
def student_topics(request):
    try:
        request.user.student
    except:
        return HttpResponse('Unauthorized', status=401)
    return render(request,'helpdesk/topics.html', {'section': 'topics', 'rol':'student'})

@login_required
def  student_new_topic_for_pdi(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewTopicForPdi(request.POST)
        # check whether it's valid:
        form
        if form.is_valid():

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            pdi_set = form.subject.pdi_set.all()

            if(len(pdi_set) == 1):
                #Create new topic
                #TODO
                return HttpResponseRedirect('/helpdesk/student/topics')
            else:
                teachers = ()
                for pdi in pdi_set:
                    teachers.append(pdi.pk, pdi.user.username)

                form = TeacherChooser(teachers)
                return render(request, 'choose_teacher.html', {'rol':'student', 'form': form})
        else:
            form = NewTopicForPdi()

    # if a GET (or any other method) we'll create a blank form
    subjects = list()

    for subject in request.user.student.subjects.all():
        subjects.append((subject.pk, subject.title))

    form = NewTopicForPdi(subjects)

    return render(request, 'helpdesk/create_topic_for_pdi.html', {'rol':'student','form': form})

@login_required
def  student_new_topic_for_pas(request):
    #TODO
    None

@login_required
def student_ask_faq(request):
    try:
        request.user.student
    except:
        return HttpResponse('Unauthorized', status=401)
    return render(request,'helpdesk/ask_faq.html', {'section': 'ask_faq','rol' : 'student' })

@login_required
def student_ask(request):
    try:
        request.user.student
    except:
        return HttpResponse('Unauthorized', status=401)
    return render(request,'helpdesk/create_topic_for_pdi.html', {'section': 'ask', 'rol' : 'student'})

@login_required
def student_topic(request, topic_id):
    try:
        request.user.student
    except:
        return HttpResponse('Unauthorized', status=401)
    topic = Topic.objects.get(pk=topic_id)
    comments = list(Comment.objects.filter(topic__id=topic_id)).order_by('date_published')
    return render(request,'helpdesk/topic.html', {'section': 'topic', 'rol' : 'student', 'topic':topic, 'comments':comments})

@login_required
def student_profile(request):
    try:
        request.user.student
    except:
        return HttpResponse('Unauthorized', status=401)

    #TODO
    return render(request,'helpdesk/student_profile.html', {'form': form, 'section': 'profile', 'rol' : 'student'})

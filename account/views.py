from django.contrib.auth.models import User
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import login

from django.http import HttpResponseRedirect

from django.http import HttpResponse

def custom_login(request):
    if request.user.is_authenticated():

        #user = User.objects.get(username=request.user)

        try:
            request.user.student
            return HttpResponseRedirect('/helpdesk/student')
        except Exception:
            try:
                request.user.pdi
                return HttpResponseRedirect('/helpdesk/pdi')
            except Exception:
                try:
                    request.user.pas
                    return HttpResponseRedirect('/helpdesk/pas')
                except Exception:
                    return HttpResponse('Unauthorized', status=401)
    else:
        #It should do something similar to code above when properly login
        return login(request)
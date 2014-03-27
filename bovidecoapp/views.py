from django.http import HttpResponseRedirect

def redirect2admin(request):
    return HttpResponseRedirect("/admin/")
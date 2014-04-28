from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def add_data(request):
    return render_to_response("add_data.html",
                            {},
                            context_instance = RequestContext(request)
    )

def redirect2admin(request):
    return HttpResponseRedirect("/admin/")


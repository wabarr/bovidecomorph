from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.models import inlineformset_factory
from django.contrib import messages
from models import *


def add_data(request, specimenID=None):
    if specimenID is None:
        messages.add_message(request, 40, 'Select a specimen to measure')
        return HttpResponseRedirect("/admin/bovidecoapp/specimen/")

    try:
        theSpecimen = specimen.objects.get(pk=specimenID)
    except:
        return HttpResponse("<h2>There is no specimen with ID#" + str(specimenID) + "<br><a href='/admin/bovidecoapp/specimen/add/'>Add A Specimen</a></h2>")

    addDataFormset = inlineformset_factory(specimen, measurement)
    if request.method == 'POST': # If the form has been submitted...
        formset = addDataFormset(request.POST)# A form bound to the POST data
        if formset.is_valid():
            formset.save()
            messages.add_message(request, messages.INFO, 'Success!.')
            return HttpResponseRedirect('/add_data/') # Redirect after POST
        else:
            messages.add_message(request, messages.INFO, 'Please correct the errors below.')


    return render_to_response("add_data.html",
                            {"formset":addDataFormset, "specimen":theSpecimen},
                            context_instance = RequestContext(request)
    )

def redirect2admin(request):
    return HttpResponseRedirect("/admin/")


from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.models import inlineformset_factory
from models import *


def add_data(request):

    addDataFormset = inlineformset_factory(specimen, measurement)
    if request.method == 'POST': # If the form has been submitted...
        formset = addDataFormset(request.POST)# A form bound to the POST data
        if formset.is_valid():
            formset.save()
            messages.add_message(request, messages.INFO, 'Success!.')
            return HttpResponseRedirect('/add_data/') # Redirect after POST
        else:
            messages.add_message(request, messages.INFO, 'Please correct the errors below.')
    else:
        theSpecimen = specimen.objects.get(pk=3606)
        formset = addDataFormset(instance = theSpecimen) # An unbound form

    return render_to_response("add_data.html",
                            {"formset":formset},
                            context_instance = RequestContext(request)
    )

def redirect2admin(request):
    return HttpResponseRedirect("/admin/")


from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.models import inlineformset_factory
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from models import *
import json

@permission_required("specimen.can_add")
def add_data(request, specimenID=None):

    if specimenID is None:
        messages.add_message(request, 40, 'Select a specimen to measure')
        return HttpResponseRedirect("/admin/bovidecoapp/specimen/")

    try:
        theSpecimen = specimen.objects.get(pk=specimenID)
    except:
        return HttpResponse("<h2>There is no specimen with ID#" + str(specimenID) + "<br><a href='/admin/bovidecoapp/specimen/add/'>Add A Specimen</a></h2>")

    try:
        pre_existing_measurements = measurement.objects.filter(specimen__exact=specimenID, MetricCharacter__element__exact = "Calcaneus")
        if pre_existing_measurements:
            messages.add_message(request, 30, 'You were redirected to the admin because this specimen already has measurements')
            return HttpResponseRedirect("/admin/bovidecoapp/specimen/" + str(specimenID))
    except:
        pass

    to_measure = MetricCharacter.objects.filter(element__exact="Calcaneus", active__exact=True).values("id")
    #to_measure = MetricCharacter.objects.filter(pk=25).values("id")
    QS_count = to_measure.count()
    to_measure = json.dumps(list(to_measure))
    addDataFormset = inlineformset_factory(specimen, measurement, can_delete = False, extra = QS_count, exclude=("comments",))
    formset_bound_to_instance = addDataFormset(instance = theSpecimen, queryset=measurement.objects.none())

    if request.method == 'POST': # If the form has been submitted...
        formset = addDataFormset(instance = theSpecimen, data = request.POST)# A form bound to the POST data
        if formset.is_valid():
            formset.save()
            messages.add_message(request, messages.INFO, 'Success!.')
            return HttpResponseRedirect('/add_data/') # Redirect after POST
        else:
            messages.add_message(request, messages.INFO, 'Please correct the errors below.')
            return render_to_response("add_data.html",
                            {"formset":formset, "specimen":theSpecimen, "to_measure":to_measure},
                            context_instance = RequestContext(request))


    return render_to_response("add_data.html",
                            {"formset":formset_bound_to_instance, "specimen":theSpecimen, "to_measure":to_measure},
                            context_instance = RequestContext(request)
    )

def redirect2admin(request):
    return HttpResponseRedirect("/admin/")


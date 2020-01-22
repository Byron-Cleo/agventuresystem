from django.shortcuts import get_object_or_404, render, redirect

from django.views.generic import TemplateView

from .forms import TransporterCreateForm, TransporterUpdateForm
from .models import TransportModel

# Create your views here.


class TransporterHomeView(TemplateView):
    template_name = "transporters/transporters_home_page.html"


def transporters_list_view(request):
    transporters = TransportModel.objects.all()
    context = {
        "transporters": transporters
    }
    template = "transporters/transporter_list_page.html"
    return render(request, template, context)


def transporter_create_view(request):
    transporter_create_form = TransporterCreateForm(request.POST or None)
    if transporter_create_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        transporter_obj = transporter_create_form.save(commit=False)
        # setting variable value/creating/assigning
        transporter_obj.created_by = request.user
        # then you can save the object in the DB
        transporter_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("transporters:transporter_list")
    else:
        transporter_create_form = TransporterCreateForm()

    context = {
        "transporter_create_form": transporter_create_form
    }
    template = "transporters/transporter_create_page.html"
    return render(request, template, context)


def transporter_detail_view(request, pk=None):
    transporter_obj = get_object_or_404(TransportModel, id=pk)
    context = {
        "transporter": transporter_obj
    }
    template = "transporters/transporter_details_page.html"
    return render(request, template, context)


def transporter_update_view(request, pk=None):
    transporter_obj = get_object_or_404(TransportModel, id=pk)
    transporter_update_form = TransporterUpdateForm(request.POST or None, instance=transporter_obj)
    context = {
        "transporter_update_form": transporter_update_form
    }
    template = "transporters/transporter_update_page.html"

    # WITHOUT THIS BLOCK OF code, the object will not be displayed on the form
    if transporter_update_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        transporter_obj = transporter_update_form.save(commit=False)
        # setting variable value/updating
        transporter_obj.updated_by = request.user
        # then you can save the object in the DB
        transporter_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("transporters:transporter_details", transporter_obj.id)

    return render(request, template, context)
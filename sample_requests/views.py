from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect

from django.views.generic import TemplateView

from .forms import SampleRequestModelCreateForm, SampleRequestUpdateForm
from .models import SampleRequestModel

# Create your views here.


class SampleRequestsHomeView(TemplateView):
    template_name = "sample_requests/sample_requests_home_page.html"


def sample_requests_list_view(request):
    sample_requests = SampleRequestModel.objects.all()
    context = {
        "sample_requests": sample_requests
    }
    template = "sample_requests/sample_requests_list_page.html"
    return render(request, template, context)


def sample_request_create_view(request):
    sample_request_create_form = SampleRequestModelCreateForm(request.POST or None)
    if sample_request_create_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        sample_request_obj = sample_request_create_form.save(commit=False)
        # setting variable value/creating/assigning
        sample_request_obj.added_by = request.user
        # then you can save the object in the DB
        sample_request_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("sample_requests:sample_requests_list")
    else:
        sample_request_create_form = SampleRequestModelCreateForm()

    context = {
        "sample_request_create_form": sample_request_create_form
    }
    template = "sample_requests/sample_request_create_page.html"
    return render(request, template, context)


def sample_request_detail_view(request, pk=None):
    sample_request_obj = get_object_or_404(SampleRequestModel, id=pk)
    context = {
        "sample_request_obj": sample_request_obj
    }
    template = "sample_requests/sample_request_details_page.html"
    return render(request, template, context)


def sample_request_update_view(request, pk=None):
    sample_request_obj = get_object_or_404(SampleRequestModel, id=pk)
    sample_request_update_form = SampleRequestUpdateForm(request.POST or None, instance=sample_request_obj)
    context = {
        "sample_request_update_form": sample_request_update_form
    }
    template = "sample_requests/sample_request_update_page.html"

    # WITHOUT THIS BLOCK OF code, the object will not be displayed on the form
    if sample_request_update_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        sample_request_obj = sample_request_update_form.save(commit=False)
        # setting variable value/updating
        sample_request_obj.updated_by = request.user
        # then you can save the object in the DB
        sample_request_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("sample_requests:sample_request_details", sample_request_obj.id)

    return render(request, template, context)
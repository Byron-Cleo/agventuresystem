from django.shortcuts import get_object_or_404, render, redirect

from django.views.generic import TemplateView

from .forms import TrailerCreateForm, TrailerUpdateForm
from .models import TrailerModel

# Create your views here.


class TrailerHomeView(TemplateView):
    template_name = "trailers/trailers_home_page.html"


def trailer_list_view(request):
    trailers = TrailerModel.objects.all()
    context = {
        "trailers": trailers
    }
    template = "trailers/trailer_list_page.html"
    return render(request, template, context)


def trailer_create_view(request):
    trailer_create_form = TrailerCreateForm(request.POST or None)
    if trailer_create_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        trailer_obj = trailer_create_form.save(commit=False)
        # setting variable value/creating/assigning
        trailer_obj.created_by = request.user
        # then you can save the object in the DB
        trailer_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("trailers:trailer_list")
    else:
        trailer_create_form = TrailerCreateForm()

    context = {
        "trailer_create_form": trailer_create_form
    }
    template = "trailers/trailer_create_page.html"
    return render(request, template, context)


def trailer_detail_view(request, pk=None):
    trailer_obj = get_object_or_404(TrailerModel, id=pk)
    context = {
        "trailer": trailer_obj
    }
    template = "trailers/trailer_details_page.html"
    return render(request, template, context)


def trailer_update_view(request, pk=None):
    trailer_obj = get_object_or_404(TrailerModel, id=pk)
    trailer_update_form = TrailerUpdateForm(request.POST or None, instance=trailer_obj)
    context = {
        "trailer_update_form": trailer_update_form
    }
    template = "trailers/trailer_update_page.html"

    # WITHOUT THIS BLOCK OF code, the object will not be displayed on the form
    if trailer_update_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        trailer_obj = trailer_update_form.save(commit=False)
        # setting variable value/updating
        trailer_obj.updated_by = request.user
        # then you can save the object in the DB
        trailer_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("trailers:trailer_details". trailer_obj.id)

    return render(request, template, context)
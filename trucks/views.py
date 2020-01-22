from django.shortcuts import get_object_or_404, render, redirect

from django.views.generic import TemplateView

from .forms import TruckCreateForm, TruckUpdateForm
from .models import TruckModel

# Create your views here.


class TruckHomeView(TemplateView):
    template_name = "trucks/trucks_home_page.html"


def truck_list_view(request):
    trucks = TruckModel.objects.all()
    context = {
        "trucks": trucks
    }
    template = "trucks/truck_list_page.html"
    return render(request, template, context)


def truck_create_view(request):
    truck_create_form = TruckCreateForm(request.POST or None)
    if truck_create_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        truck_obj = truck_create_form.save(commit=False)
        # setting variable value/creating/assigning
        truck_obj.created_by = request.user
        # then you can save the object in the DB
        truck_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("trucks:truck_list")
    else:
        truck_create_form = TruckCreateForm()

    context = {
        "truck_create_form": truck_create_form
    }
    template = "trucks/truck_create_page.html"
    return render(request, template, context)


def truck_detail_view(request, pk=None):
    truck_obj = get_object_or_404(TruckModel, id=pk)
    context = {
        "truck": truck_obj
    }
    template = "trucks/truck_details_page.html"
    return render(request, template, context)


def truck_update_view(request, pk=None):
    truck_obj = get_object_or_404(TruckModel, id=pk)
    truck_update_form = TruckUpdateForm(request.POST or None, instance=truck_obj)
    context = {
        "truck_update_form": truck_update_form
    }
    template = "trucks/truck_update_page.html"

    # WITHOUT THIS BLOCK OF code, the object will not be displayed on the form
    if truck_update_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        truck_obj = truck_update_form.save(commit=False)
        # setting variable value/updating
        truck_obj.updated_by = request.user
        # then you can save the object in the DB
        truck_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("trucks:truck_details", truck_obj.id)

    return render(request, template, context)
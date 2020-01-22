from django.shortcuts import get_object_or_404, render, redirect

from django.views.generic import TemplateView

from .forms import DriverCreateForm, DriverUpdateForm
from .models import DriverModel

# Create your views here.


class DriverHomeView(TemplateView):
    template_name = "drivers/drivers_home_page.html"


def drivers_list_view(request):
    drivers = DriverModel.objects.all()
    context = {
        "drivers": drivers
    }
    template = "drivers/driver_list_page.html"
    return render(request, template, context)


def driver_create_view(request):
    driver_create_form = DriverCreateForm(request.POST or None)
    if driver_create_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        driver_obj = driver_create_form.save(commit=False)
        # setting variable value/creating/assigning
        driver_obj.created_by = request.user
        # then you can save the object in the DB
        driver_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("drivers:driver_list")
    else:
        driver_create_form = DriverCreateForm()

    context = {
        "driver_create_form": driver_create_form
    }
    template = "drivers/driver_create_page.html"
    return render(request, template, context)


def driver_detail_view(request, pk=None):
    driver_obj = get_object_or_404(DriverModel, id=pk)
    context = {
        "driver": driver_obj
    }
    template = "drivers/driver_details_page.html"
    return render(request, template, context)


def driver_update_view(request, pk=None):
    driver_obj = get_object_or_404(DriverModel, id=pk)
    driver_update_form = DriverUpdateForm(request.POST or None, instance=driver_obj)
    context = {
        "driver_update_form": driver_update_form
    }
    template = "drivers/driver_update_page.html"

    # WITHOUT THIS BLOCK OF code, the object will not be displayed on the form
    if driver_update_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        driver_obj = driver_update_form.save(commit=False)
        # setting variable value/updating
        driver_obj.updated_by = request.user
        # then you can save the object in the DB
        driver_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("drivers:driver_details", driver_obj.id)

    return render(request, template, context)
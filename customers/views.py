from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect

from django.views.generic import TemplateView

from .forms import CustomerCreateForm, CustomerUpdateForm
from .models import CustomerModel

# Create your views here.


class CustomerHomeView(TemplateView):
    template_name = "customers/customers_home_page.html"


def customers_list_view(request):
    customers = CustomerModel.objects.all()
    context = {
        "customers": customers
    }
    template = "customers/customers_list_page.html"
    return render(request, template, context)


def customer_create_view(request):
    customer_create_form = CustomerCreateForm(request.POST or None)
    if customer_create_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        customer_obj = customer_create_form.save(commit=False)
        # setting variable value/creating/assigning
        customer_obj.added_by = request.user
        # then you can save the object in the DB
        customer_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("customers:customers_list")
    else:
        customer_create_form = CustomerCreateForm()

    context = {
        "customer_create_form": customer_create_form
    }
    template = "customers/customer_create_page.html"
    return render(request, template, context)


def customer_detail_view(request, pk=None):
    customer_obj = get_object_or_404(CustomerModel, id=pk)
    context = {
        "customer": customer_obj
    }
    template = "customers/customer_details_page.html"
    return render(request, template, context)


def customer_update_view(request, pk=None):
    customer_obj = get_object_or_404(CustomerModel, id=pk)
    customer_update_form = CustomerUpdateForm(request.POST or None, instance=customer_obj)
    context = {
        "customer_update_form": customer_update_form
    }
    template = "customers/customer_update_page.html"

    # WITHOUT THIS BLOCK OF code, the object will not be displayed on the form
    if customer_update_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        customer_obj = customer_update_form.save(commit=False)
        # setting variable value/updating
        customer_obj.updated_by = request.user
        # then you can save the object in the DB
        customer_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("customers:customer_details", customer_obj.id)

    return render(request, template, context)
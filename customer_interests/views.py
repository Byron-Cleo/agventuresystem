from django.shortcuts import get_object_or_404, render, redirect

from django.views.generic import TemplateView

from .forms import CustomerInterestCreateForm, CustomerInterestUpdateForm
from .models import CustomerInterestModel

# Create your views here.


class CustomerInterestHomeView(TemplateView):
    template_name = "customer_interests/customer_interests_home_page.html"


def customer_interests_list_view(request):
    customer_interests = CustomerInterestModel.objects.all()
    context = {
        "customer_interests": customer_interests
    }
    template = "customer_interests/customer_interest_list_page.html"
    return render(request, template, context)


def customer_interest_create_view(request):
    customer_interest_create_form = CustomerInterestCreateForm(request.POST or None)
    if customer_interest_create_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        customer_interest_obj = customer_interest_create_form.save(commit=False)
        # setting variable value/creating/assigning
        customer_interest_obj.created_by = request.user
        # then you can save the object in the DB
        customer_interest_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("customer_interests:customer_interests_list")
    else:
        customer_interest_create_form = CustomerInterestCreateForm()

    context = {
        "customer_interest_create_form": customer_interest_create_form
    }
    template = "customer_interests/customer_interest_create_page.html"
    return render(request, template, context)


def customer_interest_detail_view(request, pk=None):
    customer_interest_obj = get_object_or_404(CustomerInterestModel, id=pk)
    context = {
        "customer_interest": customer_interest_obj
    }
    template = "customer_interests/customer_interest_details_page.html"
    return render(request, template, context)


def customer_interest_update_view(request, pk=None):
    customer_interest_obj = get_object_or_404(CustomerInterestModel, id=pk)
    customer_interest_update_form = CustomerInterestUpdateForm(request.POST or None, instance=customer_interest_obj)
    context = {
        "customer_interest_update_form": customer_interest_update_form
    }
    template = "customer_interests/customer_interest_update_page.html"

    # WITHOUT THIS BLOCK OF code, the object will not be displayed on the form
    if customer_interest_update_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        customer_interest_obj = customer_interest_update_form.save(commit=False)
        # setting variable value/updating
        customer_interest_obj.updated_by = request.user
        # then you can save the object in the DB
        customer_interest_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("customer_interests:customer_interest_details", customer_interest_obj.id)

    return render(request, template, context)
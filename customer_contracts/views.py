from django.shortcuts import get_object_or_404, render, redirect

from django.views.generic import TemplateView

from .forms import CustomerContractCreateForm, CustomerContractUpdateForm
from .models import CustomerContractModel

# Create your views here.


class CustomerContractHomeView(TemplateView):
    template_name = "customer_contracts/customer_contracts_home_page.html"


def customer_contracts_list_view(request):
    customer_contracts = CustomerContractModel.objects.all()
    context = {
        "customer_contracts": customer_contracts
    }
    template = "customer_contracts/customer_contract_list_page.html"
    return render(request, template, context)


def customer_contract_create_view(request):
    customer_contract_create_form = CustomerContractCreateForm(request.POST or None)
    if customer_contract_create_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        customer_contracts_obj = customer_contract_create_form.save(commit=False)
        # setting variable value/creating/assigning
        customer_contracts_obj.created_by = request.user
        # then you can save the object in the DB
        customer_contracts_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("customer_contracts:customer_contracts_list")
    else:
        customer_contract_create_form = CustomerContractCreateForm()

    context = {
        "customer_contract_create_form": customer_contract_create_form
    }
    template = "customer_contracts/customer_contract_create_page.html"
    return render(request, template, context)


def customer_contract_detail_view(request, pk=None):
    customer_contract_obj = get_object_or_404(CustomerContractModel, id=pk)
    context = {
        "customer_contract": customer_contract_obj
    }
    template = "customer_contracts/customer_contract_details_page.html"
    return render(request, template, context)


def customer_contract_update_view(request, pk=None):
    customer_contract_obj = get_object_or_404(CustomerContractModel, id=pk)
    customer_contract_update_form = CustomerContractUpdateForm(request.POST or None, instance=customer_contract_obj)
    context = {
        "customer_contract_update_form": customer_contract_update_form
    }
    template = "customer_contracts/customer_contract_update_page.html"

    # WITHOUT THIS BLOCK OF code, the object will not be displayed on the form
    if customer_contract_update_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        customer_contract_obj = customer_contract_update_form.save(commit=False)
        # setting variable value/updating
        customer_contract_obj.updated_by = request.user
        # then you can save the object in the DB
        customer_contract_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("customer_contracts:customer_contract_details", customer_contract_obj.id)

    return render(request, template, context)
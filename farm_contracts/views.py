from django.shortcuts import get_object_or_404, render, redirect

from django.views.generic import TemplateView

from .forms import FarmContractCreateForm, FarmContractUpdateForm
from .models import FarmContractModel

# Create your views here.


class FarmContractHomeView(TemplateView):
    template_name = "farm_contracts/farm_contracts_home_page.html"


def farm_contracts_list_view(request):
    customer_contracts = FarmContractModel.objects.all()
    context = {
        "farm_contracts": customer_contracts
    }
    template = "farm_contracts/farm_contract_list_page.html"
    return render(request, template, context)


def farm_contract_create_view(request):
    farm_contract_create_form = FarmContractCreateForm(request.POST or None)
    if farm_contract_create_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        farm_contract_obj = farm_contract_create_form.save(commit=False)
        # setting variable value/creating/assigning
        farm_contract_obj.created_by = request.user
        # then you can save the object in the DB
        farm_contract_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("farm_contracts:farm_contracts_list")
    else:
        farm_contract_create_form = FarmContractCreateForm()

    context = {
        "farm_contract_create_form": farm_contract_create_form
    }
    template = "farm_contracts/farm_contract_create_page.html"
    return render(request, template, context)


def farm_contract_detail_view(request, pk=None):
    farm_contract_obj = get_object_or_404(FarmContractModel, id=pk)
    context = {
        "farm_contract": farm_contract_obj
    }
    template = "farm_contracts/farm_contract_details_page.html"
    return render(request, template, context)


def farm_contract_update_view(request, pk=None):
    farm_contract_obj = get_object_or_404(FarmContractModel, id=pk)
    farm_contract_update_form = FarmContractUpdateForm(request.POST or None, instance=farm_contract_obj)
    context = {
        "farm_contract_update_form": farm_contract_update_form
    }
    template = "farm_contracts/farm_contract_update_page.html"

    # WITHOUT THIS BLOCK OF code, the object will not be displayed on the form
    if farm_contract_update_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        farm_contract_obj = farm_contract_update_form.save(commit=False)
        # setting variable value/updating
        farm_contract_obj.updated_by = request.user
        # then you can save the object in the DB
        farm_contract_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("farm_contracts:farm_contract_details", farm_contract_obj.id)

    return render(request, template, context)
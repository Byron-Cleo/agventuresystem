from django.shortcuts import get_object_or_404, render, redirect

from django.views.generic import TemplateView

from .forms import CustomerPaymentCreateForm, CustomerPaymentUpdateForm
from .models import CustomerPaymentModel

# Create your views here.


class CustomerPaymentHomeView(TemplateView):
    template_name = "customer_payments/customer_payments_home_page.html"


def customer_pay_list_view(request):
    customer_payments = CustomerPaymentModel.objects.all()
    context = {
        "customer_payments": customer_payments
    }
    template = "customer_payments/customer_payment_list_page.html"
    return render(request, template, context)


def customer_pay_create_view(request):
    customer_pay_create_form = CustomerPaymentCreateForm(request.POST or None)
    if customer_pay_create_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        cust_payment_obj = customer_pay_create_form.save(commit=False)
        # setting variable value/creating/assigning
        cust_payment_obj.created_by = request.user
        # then you can save the object in the DB
        cust_payment_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("customer_payments:customer_payments_list")
    else:
        customer_pay_create_form = CustomerPaymentCreateForm()

    context = {
        "customer_pay_create_form": customer_pay_create_form
    }
    template = "customer_payments/customer_payments_create_page.html"
    return render(request, template, context)


def customer_pay_detail_view(request, pk=None):
    cust_payment_obj = get_object_or_404(CustomerPaymentModel, id=pk)
    context = {
        "cust_payment_obj": cust_payment_obj
    }
    template = "customer_payments/customer_payment_details_page.html"
    return render(request, template, context)


def customer_pay_update_view(request, pk=None):
    cust_payment_obj = get_object_or_404(CustomerPaymentModel, id=pk)
    customer_pay_update_form = CustomerPaymentUpdateForm(request.POST or None, instance=cust_payment_obj)
    context = {
        "customer_pay_update_form": customer_pay_update_form
    }
    template = "customer_payments/customer_payment_update_page.html"

    # WITHOUT THIS BLOCK OF code, the object will not be displayed on the form
    if customer_pay_update_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        cust_payment_obj = customer_pay_update_form.save(commit=False)
        # setting variable value/updating
        cust_payment_obj.updated_by = request.user
        # then you can save the object in the DB
        cust_payment_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("customer_payments:customer_payment_details", cust_payment_obj.id)

    return render(request, template, context)
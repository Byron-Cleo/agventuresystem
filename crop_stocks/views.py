from django.shortcuts import get_object_or_404, render, redirect

from django.views.generic import TemplateView

from .forms import CropStockCreateForm, CropStockUpdateForm
from .models import CropStockModel

# Create your views here.


class CropStockHomeView(TemplateView):
    template_name = "crop_stocks/crop_stocks_home_page.html"


def crop_stocks_list_view(request):
    crop_stocks = CropStockModel.objects.all()
    context = {
        "crop_stocks": crop_stocks
    }
    template = "crop_stocks/crops_stock_list_page.html"
    return render(request, template, context)


def crop_stock_create_view(request):
    crop_stock_create_form = CropStockCreateForm(request.POST or None)
    if crop_stock_create_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        crop_stock_obj = crop_stock_create_form.save(commit=False)
        # setting variable value/creating/assigning
        crop_stock_obj.added_by = request.user
        # then you can save the object in the DB
        crop_stock_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("crop_stocks:crops_stock_list")
    else:
        crop_stock_create_form = CropStockCreateForm()

    context = {
        "crop_stock_create_form": crop_stock_create_form
    }
    template = "crop_stocks/crop_stock_create_page.html"
    return render(request, template, context)


def crop_stock_detail_view(request, pk=None):
    crop_stock_obj = get_object_or_404(CropStockModel, id=pk)
    context = {
        "crop_stock": crop_stock_obj
    }
    template = "crop_stocks/crop_stock_details_page.html"
    return render(request, template, context)


def crop_stock_update_view(request, pk=None):
    crop_stock_obj = get_object_or_404(CropStockModel, id=pk)
    crop_stock_update_form = CropStockUpdateForm(request.POST or None, instance=crop_stock_obj)
    context = {
        "crop_stock_update_form": crop_stock_update_form
    }
    template = "crop_stocks/crop_stock_update_page.html"

    # WITHOUT THIS BLOCK OF code, the object will not be displayed on the form
    if crop_stock_update_form.is_valid():
        # if all updated data are valid, DON'T SAVE FIRST
        crop_stock_obj = crop_stock_update_form.save(commit=False)
        # setting variable value/updating
        crop_stock_obj.updated_by = request.user
        # then you can save the object in the DB
        crop_stock_obj.save()
        # After saving go back to the details page to view you updated data
        return redirect("crop_stocks:crop_stock_details", crop_stock_obj.id)

    return render(request, template, context)
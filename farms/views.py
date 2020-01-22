from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, Http404

from .forms import FarmCreateForm, FarmUpdateForm
from .models import FarmModel


# Create your views here.
class FarmHomeView(TemplateView):
    template_name = "farms/farm_home_page.html"


def farms_list_view(request):
    farms = FarmModel.objects.all()
    context = {
        "farms": farms
    }
    template = "farms/farms_list_page.html"
    return render(request, template, context)


def farm_create_view(request):
    print(request.POST)
    form = FarmCreateForm(request.POST or None)
    if form.is_valid():
        farm_obj = form.save(commit=False)
        farm_obj.added_by = request.user
        farm_obj.save()
        return redirect('farms:farms_list')
    else:
        form = FarmCreateForm()
    context = {
        "form": form
    }
    template = "farms/farm_create_page.html"
    return render(request, template, context)


def farm_detail_view(request, pk=None):
    farm_obj = get_object_or_404(FarmModel, id=pk)
    context = {
        "farm": farm_obj
    }
    template = "farms/farm_details_page.html"
    return render(request, template, context)


def farm_update_view(request, **kwargs):
    farm_obj = get_object_or_404(FarmModel, **kwargs)
    form = FarmUpdateForm(request.POST or None, instance=farm_obj)
    context = {
        "form": form
    }
    if form.is_valid():
        farm_obj = form.save(commit=False)
        farm_obj.updated_by = request.user
        farm_obj.save()
        return redirect('farms:farm_details', farm_obj.id)
    template = "farms/farm_update_page.html"
    return render(request, template, context)


# def farm_delete_view(request, pk=None):
#     crop = get_object_or_404(FarmModel, id=pk)
#     # try:
#     #     crop = Cropstock.objects.get(id=id)
#     # except Cropstock.DoesNotExist:
#     #     raise Http404("Product doesn't exist")
#
#     # cropobj = Cropstock.objects.filter(id=pk)
#     # if cropobj.exists() and cropobj.count() == 1:
#     #     crop = cropobj.first()
#     # else:
#     #     raise Http404("Product doesn't exist")
#     if request.method == "POST":
#         crop.delete()
#         messages.success(request, "Crop Deleted by {user}".format(user=request.user))
#         return redirect('crops:crop_list')
#     context = {
#             "crop": crop
#     }
#     template = "farms/farm_delete.html"
#     return render(request, template, context)
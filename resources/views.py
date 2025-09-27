from django.shortcuts import render, redirect
from .forms import ResourceForm
from .models import Resource

def upload_resource(request):
    if request.method == "POST":
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("resource_list")
    else:
        form = ResourceForm()
    return render(request, "resources/upload.html", {"form": form})


def resource_list(request):
    resources = Resource.objects.all().order_by("-uploaded_at")
    return render(request, "resources/list.html", {"resources": resources})


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

    # GET params
    query = request.GET.get("search", "")
    category_filter = request.GET.get("category", "")

    # Search by title
    if query:
        resources = resources.filter(title__icontains=query)

    # Filter by category (assuming category is ForeignKey id)
    if category_filter:
        resources = resources.filter(category_id=category_filter)

    # Get unique categories for dropdown
    categories = Resource.objects.values_list('category_id', flat=True).distinct()

    return render(request, "resources/list.html", {
        "resources": resources,
        "query": query,
        "categories": categories,
        "category_filter": int(category_filter) if category_filter else ""
    })

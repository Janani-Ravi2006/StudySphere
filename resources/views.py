from django.shortcuts import render, get_object_or_404, redirect
from .models import Resource, Comment, Rating
from .forms import CommentForm, RatingForm
from django.db.models import Avg

# Step 1: Add this function
def resource_list(request):
    resources = Resource.objects.all()  # Get all resources
    return render(request, 'resources/resource_list.html', {
        'resources': resources
    })

# Existing function
def resource_detail(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    comments = resource.comments.all()
    ratings = resource.ratings.all()
    average_rating = ratings.aggregate(Avg('score'))['score__avg']

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        rating_form = RatingForm(request.POST)
        if comment_form.is_valid() and rating_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.resource = resource
            comment.save()

            rating = rating_form.save(commit=False)
            rating.user = request.user
            rating.resource = resource
            rating.save()

            return redirect('resource_detail', resource_id=resource.id)
    else:
        comment_form = CommentForm()
        rating_form = RatingForm()

    return render(request, 'resources/resource_detail.html', {
        'resource': resource,
        'comments': comments,
        'average_rating': round(average_rating, 1) if average_rating else None,
        'comment_form': comment_form,
        'rating_form': rating_form
    })

# portal/views.py
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.http import HttpResponseForbidden
from .forms import UserRegisterForm, ProfileUpdateForm, LostItemForm, FoundItemForm
from .models import Profile, LostItem, FoundItem, ItemHistory

def home(request):
    lost_items = LostItem.objects.filter(returned=False).order_by('-date_lost')
    found_items = FoundItem.objects.filter(returned=False).order_by('-date_found')
    return render(request, 'portal/home.html', {
        'lost_items': lost_items,
        'found_items': found_items
    })

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'portal/register.html', {'form': form})

@login_required
def profile(request):
    # ensure profile exists
    Profile.objects.get_or_create(user=request.user, defaults={'full_name': request.user.username})
    instance = request.user.profile
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=instance)
    return render(request, 'portal/profile.html', {'form': form})

@login_required
def post_lost_item(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('home')
    else:
        form = LostItemForm()
    return render(request, 'portal/post_lost_item.html', {'form': form})

@login_required
def post_found_item(request):
    if request.method == 'POST':
        form = FoundItemForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('home')
    else:
        form = FoundItemForm()
    return render(request, 'portal/post_found_item.html', {'form': form})

def lost_detail(request, pk):
    item = get_object_or_404(LostItem, pk=pk)
    return render(request, 'portal/item_detail.html', {'item': item, 'kind': 'lost'})

def found_detail(request, pk):
    item = get_object_or_404(FoundItem, pk=pk)
    return render(request, 'portal/item_detail.html', {'item': item, 'kind': 'found'})

@login_required
def claim_lost_item(request, pk):
    item = get_object_or_404(LostItem, pk=pk, returned=False)
    if not item.is_claimed:
        item.is_claimed = True
        item.claimed_by = request.user
        item.save()
    return redirect('lost_detail', pk=item.pk)

@login_required
def claim_found_item(request, pk):
    item = get_object_or_404(FoundItem, pk=pk, returned=False)
    if not item.is_claimed:
        item.is_claimed = True
        item.claimed_by = request.user
        item.save()
    return redirect('found_detail', pk=item.pk)

@user_passes_test(lambda u: u.is_staff)
def mark_returned(request, item_type, pk):
    if item_type not in ('Lost', 'Found'):
        return HttpResponseForbidden("Invalid item type")

    if item_type == 'Lost':
        src = get_object_or_404(LostItem, pk=pk, returned=False)
        ItemHistory.objects.create(
            title=src.title, description=src.description, category=src.category,
            location=src.location, image=src.image, original_user=src.user,
            date_posted=src.date_lost, item_type='Lost'
        )
        src.returned = True
        src.save()
        return redirect('lost_detail', pk=src.pk)
    else:
        src = get_object_or_404(FoundItem, pk=pk, returned=False)
        ItemHistory.objects.create(
            title=src.title, description=src.description, category=src.category,
            location=src.location, image=src.image, original_user=src.user,
            date_posted=src.date_found, item_type='Found'
        )
        src.returned = True
        src.save()
        return redirect('found_detail', pk=src.pk)

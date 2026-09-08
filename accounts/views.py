from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import StaffMember
from .forms import StaffMemberForm
from django.shortcuts import get_object_or_404
@login_required
def home(request):
    return render(request, 'home.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def staff_list(request):
    staff = StaffMember.objects.all()
    return render(request, 'staff_list.html', {'staff': staff})

def add_staff(request):
    if request.method == 'POST':
        form = StaffMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffMemberForm()
    return render(request, 'add_staff.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404

def edit_staff(request, pk):
    staff = get_object_or_404(StaffMember, pk=pk)
    if request.method == 'POST':
        form = StaffMemberForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffMemberForm(instance=staff)
    return render(request, 'add_staff.html', {'form': form})

def delete_staff(request, pk):
    staff = get_object_or_404(StaffMember, pk=pk)
    if request.method == 'POST':
        staff.delete()
        return redirect('staff_list')
    return render(request, 'confirm_delete.html', {'staff': staff})


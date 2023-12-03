from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from realtors.app_forms import UserForm, RealtorForm
from realtors.models import User, Realtor


# Create your views here.
# def users(request):
#     return None
@login_required
@permission_required('webapp.add_user', raise_exception=True)
def user(request):
    user = User.objects.all()
    paginator = Paginator(user, 10)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    return render(request, 'user.html', {"user": data})


def all_users(request):
    user = User.objects.all()
    # user = User.objects.filter(user_type="landlord")
    # user = User.objects.filter(user_type="student")
    paginator = Paginator(user, 10)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    return render(request, 'all_users.html', {"user": data})


@login_required
@permission_required('webapp.view_user', raise_exception=True)
def user_details(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'user_details.html', {"user": user})


@login_required
# @permission_required('webapp.add_user', raise_exception=True)
def user_delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    messages.warning(request, "The user was deleted permanently")
    return redirect("all")


@login_required
@permission_required('webapp.change_user', raise_exception=True)
def user_update(request, user_id):
    user = get_object_or_404(User, pk=user_id)  # SELECT * FROM employees WHERE id=1
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully")
            return redirect('details', user_id)

    else:
        form = UserForm(instance=user)

    return render(request, "update.html", {"form": form})


# def user(request):
#     return None
@login_required
@permission_required('main_app.view_user', raise_exception=True)
def search_user(request):
    search_word = request.GET["search_word"]
    employees = User.objects.filter(
        Q(name__icontains=search_word) | Q(email__icontains=search_word)
    )
    paginator = Paginator(employees, 20)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    # Elastic search
    return render(request, "all_users.html", {"user": data})


@login_required
@permission_required('webapp.add_realtor', raise_exception=True)
def realtor(request):
    realtor = Realtor.objects.all()
    paginator = Paginator(realtor, 10)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    return render(request, 'realtor.html', {"realtor": data})


def all_realtors(request):
    realtor = Realtor.objects.all()
    # user = User.objects.filter(user_type="landlord")
    # user = User.objects.filter(user_type="student")
    paginator = Paginator(realtor, 10)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    return render(request, 'all_realtors.html', {"realtor": data})


@login_required
@permission_required('main_app.view_realtor', raise_exception=True)
def search_realtor(request):
    search_word = request.GET["search_word"]
    realtor = Realtor.objects.filter(
        Q(name__icontains=search_word) | Q(email__icontains=search_word)
    )
    paginator = Paginator(realtor, 10)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    # Elastic search
    return render(request, "all_realtors.html", {"realtor": data})

@login_required
@permission_required('webapp.view_realtor', raise_exception=True)
def realtor_details(request, realtor_id):
    realtor = Realtor.objects.get(pk=realtor_id)
    return render(request, 'realtor_details.html', {"realtor": realtor})

@login_required
# @permission_required('webapp.remove_realtor', raise_exception=True)
def realtor_delete(request, realtor_id):
    realtor = get_object_or_404(User, pk=realtor_id)
    realtor.delete()
    messages.warning(request, "The realtor was deleted permanently")
    return redirect("all")


def realtor_update(request, realtor_id):
    realtor = get_object_or_404(User, pk=realtor_id)  # SELECT * FROM employees WHERE id=1
    if request.method == "POST":
        form = RealtorForm(request.POST, request.FILES, instance=realtor)
        if form.is_valid():
            form.save()
            messages.success(request, "Realtor updated successfully")
            return redirect('details', realtor_id)

    else:
        form = RealtorForm(instance=user)

    return render(request, "update.html", {"form": form})


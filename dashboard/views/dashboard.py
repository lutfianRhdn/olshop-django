from django.shortcuts import render, redirect, HttpResponse, get_object_or_404


def dashboard(request):
    return render(request, 'admin/dashboard.html')


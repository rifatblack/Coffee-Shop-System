from django.shortcuts import render

def about(request):
    return render(request, "about.html")

def my_custom_permission_denied_view(request, exception):
    return render(request, "403.html")
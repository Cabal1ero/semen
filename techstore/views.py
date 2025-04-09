from django.shortcuts import render

def home(request):
    """
    Представление для домашней страницы.
    """
    return render(request, 'page/home.html')

def computers(request):
    """
    Представление для страницы компьютеров.
    """
    return render(request, 'page/computer.html')

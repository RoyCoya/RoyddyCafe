import imp
from django.shortcuts import render


from django.shortcuts import render

def homepage(request):
    return render(request, 'AchievementNet/homepage/homepage.html')
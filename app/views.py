from django.shortcuts import render

# Create your views here.
# landing page view
def LandingPage(request):
    return render(request, 'index.html')
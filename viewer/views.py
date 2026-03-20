from django.shortcuts import render

# 1. New Landing Page
def landing_page(request):
    return render(request, "landing.html")

# 2. Mobile / ngrok (model-viewer)
def mobile_view(request):
    return render(request, "index.html")

# 3. Laptop (AR.js + Marker)
def laptop_view(request):
    return render(request, "laptop_ar.html")
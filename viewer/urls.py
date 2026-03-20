from django.urls import path
from . import views

urlpatterns = [
    # The main landing page (http://127.0.0.1:8000/)
    path('', views.landing_page, name='landing'),

    # Mobile AR (http://127.0.0.1:8000/mobile/)
    path('mobile/', views.mobile_view, name='mobile_ar'),

    # Laptop AR (http://127.0.0.1:8000/laptop_ar/)
    path('laptop_ar/', views.laptop_view, name='laptop_ar'),
]
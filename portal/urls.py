# portal/urls.py
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Auth
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='portal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    # Profile
    path('profile/', views.profile, name='profile'),

    # Create items
    path('post-lost/', views.post_lost_item, name='post_lost_item'),
    path('post-found/', views.post_found_item, name='post_found_item'),

    # Detail pages
    path('lost/<int:pk>/', views.lost_detail, name='lost_detail'),
    path('found/<int:pk>/', views.found_detail, name='found_detail'),

    # Claim and admin-return
    path('claim-lost/<int:pk>/', views.claim_lost_item, name='claim_lost_item'),
    path('claim-found/<int:pk>/', views.claim_found_item, name='claim_found_item'),
    path('return/<str:item_type>/<int:pk>/', views.mark_returned, name='mark_returned'),
]

from django.urls import path, include
from . import views
urlpatterns = [
    path('user-type/redirect/', views.UserTypeRedirectView.as_view(), name='user_type_redirect'),
]

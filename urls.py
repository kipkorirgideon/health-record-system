from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

import views

urlpatterns = [
    path('', login_required(views.HomePageView.as_view(), login_url='/accounts/login/'), name='home'),
    path('records/', include('records.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include

import accounts.views
import views

urlpatterns = [
    path('', accounts.views.UserTypeRedirectView.as_view(), name='home'),
    path('dashboard/', accounts.views.DashboardView.as_view(), name='dashboard'),
    path('records/', include('records.urls')),
    path('accounts/', include('allauth.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
]

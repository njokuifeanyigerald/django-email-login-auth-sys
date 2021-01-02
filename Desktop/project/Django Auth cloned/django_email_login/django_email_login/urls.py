from django.contrib import admin
from django.urls import path,include

from accounts.views import LoginView, RegisterView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls'))
]

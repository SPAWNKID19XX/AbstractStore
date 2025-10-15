from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse, request

def home_test_server_running(request):
    return HttpResponse("Server is running")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_test_server_running),
    path('users/api/v1/', include('users.urls'))
]

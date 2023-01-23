from django.urls import path
from .views import signup, home, tasks, logout_user

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path("tasks/", tasks, name="tasks"),
    path("logout/", logout_user, name="logout")
]

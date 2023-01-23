from django.urls import path
from .views import signup, home, tasks

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path("tasks/", tasks, name="tasks")
]

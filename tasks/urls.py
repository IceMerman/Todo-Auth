from django.urls import path
from .views import signup, home, tasks, logout_user, signin

urlpatterns = [
    path('', home, name='home'),
    path("tasks/", tasks, name="tasks"),
    path('signup/', signup, name='sign_up'),
    path("logout/", logout_user, name="logout"),
    path("signin/", signin, name="sign_in")
]   

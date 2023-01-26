from django.urls import path
from .views import signup, home, tasks, logout_user, signin, create_task, task_detail, task_complete, task_delete, tasks_completed

urlpatterns = [
    path('', home, name='home'),
    path("tasks/", tasks, name="tasks"),
    path("tasks/completed", tasks_completed, name="tasks_completed"),
    path('task/create/', create_task, name='create_task'),
    path("task/<int:id_task>/", task_detail, name="task_detail"),
    path("task/<int:id_task>/complete/", task_complete, name="task_complete"),
    path("task/<int:id_task>/delete/", task_delete, name="task_delete"),
    path('signup/', signup, name='sign_up'),
    path("logout/", logout_user, name="logout"),
    path("signin/", signin, name="sign_in")
]

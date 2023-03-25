import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse

from .models import Task
from django.contrib.auth.models import User

class TaskModelTest(TestCase):
    
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_has_invalid_dates(self) -> None:
        """This test create a task with a creatin date posterior to the completation date the assert must be false"""
        new_creation_time = timezone.now() + datetime.timedelta(days=30)
        new_completation_time = timezone.now()
        test_user = User.objects.create(username="Test_User", password="Test_pwd")

        test_task = Task(title="Test task", 
                         description="Testing tasking", 
                         created=new_creation_time, 
                         date_completed=new_completation_time,
                         important=False,
                         user=test_user)
        
        self.assertFalse(test_task.hasValidDates())

    
class testHomeView(TestCase):

    def test_home_content(self):
        """Test home page containts lorem ipsums in its content"""
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'Lorem')
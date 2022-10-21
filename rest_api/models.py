from email.policy import default
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Friends(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user', null=False, blank=False)

    friend_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='friend', null=False, blank=False)

    def __str__(self):
        return self.user_id.name


class Lessons(models.Model):
    title = models.CharField(max_length=50)
    student_id = models.ForeignKey(
        User, related_name='lessons', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.title
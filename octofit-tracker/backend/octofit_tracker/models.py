from djongo import models
from django.contrib.auth import get_user_model

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.user.username

class Activity(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    calories = models.IntegerField()
    def __str__(self):
        return f"{self.user_profile.user.username} - {self.type}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team.name} - {self.points}"

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, UserProfile, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = UserProfile.objects.create(user=self.user, team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', duration=30)
        self.activity = Activity.objects.create(user_profile=self.profile, type='Run', duration=20, calories=200)
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_team(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_user_profile(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.team, self.team)

    def test_activity(self):
        self.assertEqual(self.activity.type, 'Run')
        self.assertEqual(self.activity.calories, 200)

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Test Workout')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.points, 100)

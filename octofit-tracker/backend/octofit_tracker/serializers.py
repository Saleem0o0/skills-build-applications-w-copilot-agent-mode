from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Team, UserProfile, Activity, Workout, Leaderboard

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    team = TeamSerializer()
    class Meta:
        model = UserProfile
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()
    class Meta:
        model = Activity
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class LeaderboardSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    class Meta:
        model = Leaderboard
        fields = '__all__'

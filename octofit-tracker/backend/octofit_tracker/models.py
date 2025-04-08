from bson import ObjectId
from djongo import models

class ObjectIdField(models.Field):
    def get_prep_value(self, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value

class User(models.Model):
    id = ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Team(models.Model):
    id = ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100, unique=True)
    members = models.JSONField()

class Activity(models.Model):
    id = ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    activity_id = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

class Leaderboard(models.Model):
    id = ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    leaderboard_id = models.CharField(max_length=100, unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    id = ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    workout_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    duration = models.IntegerField()

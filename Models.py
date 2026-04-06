from django.db import models

class Voter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

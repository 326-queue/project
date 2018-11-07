from django.db import models
from django.urls import reverse

class Hackathon(models.Model):
    fundraising_goal = models.IntegerField()
    total_funding_raised = models.IntegerField
    fundraising_deadline = models.DateField()
    hackathon_date = models.DateField()
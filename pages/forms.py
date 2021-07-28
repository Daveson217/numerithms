from django import forms
from django.db import models

class FractionalKnapsackForm(forms.Form):
    profits = models.CharField(blank=False)
    weights = models.CharField(blank=False)
    max_weight = models.CharField(blank=False)


class JobSequencingDeadlineForm(forms.Form):
    jobs = models.CharField(blank=False)
    deadlines = models.CharField(blank=False)
    profits = models.CharField(blank=False)
    
    
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=100,null=True, blank=True)
    height = models.FloatField()
    weight = models.FloatField()
    bmi = models.FloatField(null=True, blank=True)  # Add BMI field

    def save(self, *args, **kwargs):
        if self.height and self.weight:
            self.bmi = self.calculate_bmi()
        super().save(*args, **kwargs)

    def calculate_bmi(self):
        return round(self.weight / ((self.height / 100) ** 2),2)

from django.db import models

class Application(models.Model):
    application_id = models.CharField(max_length=25, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    entrance_exam = models.CharField(max_length=50)
    score = models.FloatField()
    institution = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)

    status = models.CharField(max_length=20, default="SUBMITTED")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.application_id

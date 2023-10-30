from django.db import models
import datetime
class Author(models.Model):
    name = models.CharField(max_length=45)
    age = models.PositiveSmallIntegerField(default=20)
    course = models.PositiveSmallIntegerField(default=1)
    student_id  = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.name

class Plan(models.Model):
    title = models.CharField(max_length=100)
    sana = models.DateField(default=datetime.date.today())
    dt_info = models.TextField(blank=True, null=True)
    done = models.BooleanField(default=False)
    student_fk = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.student_fk}"
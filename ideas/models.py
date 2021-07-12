from django.db import models

IDEA_STATUS = (
    ('pending','Waiting for review'),
    ('accepted', 'Accepted'),
    ('done', 'Done'),
    ('rejected', 'Rejected')
)

# Create your models here.


class Idea(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    youtube_url = models.URLField(null=True, blank=True)
    status = models.CharField(max_length=255, choices=IDEA_STATUS, default='pending')


    def __str__(self):
        return self.title

class Vote(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self):
        return f'ID {self.id}'

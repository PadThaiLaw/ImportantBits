from django.db import models

# Create your models here.
class Citation(models.Model):
    canlii_id = models.CharField(max_length=50)
    paragraph_num = models.PositiveIntegerField()
    citation_count = models.PositiveIntegerField()
    sentiment_sum = models.IntegerField()

    def __str__(self):
        return self.canlii_id + " para. " + str(self.paragraph_num)
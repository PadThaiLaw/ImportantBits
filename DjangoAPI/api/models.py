from django.db import models

# Create your models here.

class Decision(models.Model):
    canlii_id = models.CharField(max_length = 100)
    name = models.CharField(max_length = 500)
    neutral_citation = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Citation(models.Model):
    cited_case_id = models.ForeignKey(Decision, related_name="cited_case", on_delete = models.PROTECT)
    citing_case_id = models.ForeignKey(Decision, related_name="citing_case", on_delete = models.PROTECT)

    def __str__(self):
        return self.cited_case_id.name + " " + self.citing_case_id.name

class Paragraph(models.Model):
    citation_id = models.ForeignKey(Citation, on_delete = models.PROTECT)
    cited_paragraph = models.PositiveIntegerField()
    citing_paragraph = models.PositiveIntegerField()
    sentiment_score = models.DecimalField(decimal_places=10, max_digits=12)

    def __str__(self):
        return self.citation_id.cited_case_id.name + " " + self.citation_id.citing_case_id.name + " " + str(self.cited_paragraph)
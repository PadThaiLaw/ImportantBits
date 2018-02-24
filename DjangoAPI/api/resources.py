from tastypie.resources import ModelResource
from api.models import Decision, Citation, Paragraph


class CitationResource(ModelResource):
    class Meta:
        # object_list = Decision.objects.filter(canlii_id = "2001scc2")
        queryset = Paragraph.objects.all()
        resource_name = 'citation'

# # Create your models here.

# class Decision(models.Model):
#     case_id_canlii = models.CharField(max_length = 100)
#     case_name = models.CharField(max_length = 500)
#     case_neutral_citation = models.CharField(max_length = 100)

#     def __str__(self):
#         return self.case_name

# class Citation(models.Model):
#     cited_case_id = models.ForeignKey(Decision, related_name="cited_case", on_delete = models.PROTECT)
#     citing_case_id = models.ForeignKey(Decision, related_name="citing_case", on_delete = models.PROTECT)

#     def __str__(self):
#         return self.cited_case_id.case_name + " " + self.citing_case_id.case_name

# class Paragraph(models.Model):
#     citing_case_id = models.ForeignKey(Citation, on_delete = models.PROTECT)
#     cited_paragraph = models.PositiveIntegerField()
#     citing_paragraph = models.PositiveIntegerField()

#     def __str__(self):
#         return self.cited_paragraph
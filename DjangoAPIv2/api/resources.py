from tastypie import fields
from tastypie.resources import ModelResource
from api.models import Decision, Citation, Paragraph

class DecisionResource(ModelResource):
    class Meta:
        # object_list = Decision.objects.filter(canlii_id = "2001scc2")
        queryset = Decision.objects.all()
        resource_name = 'decision'
        

class CitationResource(ModelResource):
    cited_case_id = fields.ForeignKey(DecisionResource, 'cited_case_id')
    class Meta:
        # object_list = Decision.objects.filter(canlii_id = "2001scc2")
        queryset = Citation.objects.all()
        resource_name = 'citation'

class ParagraphResource(ModelResource):
    citation_id = fields.ForeignKey(CitationResource, 'citation_id')
    sentscore = fields.DecimalField(readonly=True)
    class Meta:
        # object_list = Decision.objects.filter(canlii_id = "2001scc2")
        input_canlii_id = '2001scc2'
        queryset = Paragraph.objects.all().filter(citation_id = Citation.objects.all().filter(cited_case_id = Decision.objects.get(canlii_id = input_canlii_id)))
        resource_name = 'paragraph'

        def dehydrate_sentscore(self, bundle):
                average_score = 0.0
                for para in bundle.obj.sentiment_score.all():
                    average_score = 10000.000
                return average_score


        # choose field names to include
        # fields = ['cited_paragraph', 'sentiment_score']


        # # http://django-tastypie.readthedocs.org/en/latest/resources.html#alter-list-data-to-serialize
        # def alter_list_data_to_serialize(self, request, data):
        #     if request.GET.get('meta_only'):
        #         return {'meta': data['meta']}
        #     return data

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
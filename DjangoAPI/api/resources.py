from tastypie.resources import ModelResource
from api.models import Citation
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from tastypie import fields

class CitationResource(ModelResource):
    class Meta:
        include_resource_uri = False
        queryset = Citation.objects.all()
        resource_name = 'citation'
        authorization = Authorization()
        filtering = {
            'canlii_id': ALL
        }
        fields = ['canlii_id', 'paragraph_num', 'citation_count', 'sentiment_sum']

    def dehydrate(self, bundle):
        if 'canlii_id' in bundle.data.keys():
            del bundle.data['canlii_id']
        return bundle
    
    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                # Get rid of the "meta".
                del(data_dict['meta'])

        return data_dict
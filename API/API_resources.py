from tastypie.resources import ModelResource, ALL_WITH_RELATIONS, ALL
from tastypie.authentication import ApiKeyAuthentication
from tastypie import fields

from bovidecoapp.models import MetricCharacter, museum, collection, measurement, taxonomy, specimen
from API.serializers import CSVSerializer


class TaxonomyResource(ModelResource):
    class Meta:
        queryset = taxonomy.objects.all()
        allowed_methods=['get']
        excludes = ["synonyms", "commonName", "kingdon", "phylum", "tclass"]
        resource_name = "taxonomy"
        filtering = {
            "tribe": ALL,
            "family":ALL,
        }
        serializer = CSVSerializer()
        max_limit = 0
        authentication = ApiKeyAuthentication()

class MetricCharacterResource(ModelResource):
    class Meta:
        queryset = MetricCharacter.objects.all()
        allowed_methods=['get']
        fields = ["code", "element"]
        resource_name = 'MetricCharacter'
        filtering = {
            "code": ALL,
            "element":ALL,
        }
        serializer = CSVSerializer()
        max_limit=0
        authentication = ApiKeyAuthentication()

class MuseumResource(ModelResource):
    class Meta:
        queryset = museum.objects.all()
        allowed_methods=['get']
        fields = ["code"]
        resource_name = "museum"
        serializer = CSVSerializer()
        max_limit=0
        authentication = ApiKeyAuthentication()

class CollectionResource(ModelResource):
    museum = fields.ForeignKey(MuseumResource, "museum")
    class Meta:
        queryset = collection.objects.all()
        allowed_methods=['get']
        fields=["code"]
        resource_name = "collection"
        serializer = CSVSerializer()
        max_limit=0
        authentication = ApiKeyAuthentication()

class MeasurementResource(ModelResource):
    specimen = fields.ForeignKey("API.API_resources.SpecimenResource", "specimen", full=True)
    MetricCharacter = fields.ForeignKey(MetricCharacterResource, "MetricCharacter", full=True)
    class Meta:
        queryset = measurement.objects.all()
        allowed_methods = ['get']
        resource_name = "measurement"
        filtering = {
            "MetricCharacter": ALL_WITH_RELATIONS,
            "taxon": ALL_WITH_RELATIONS,
        }
        serializer = CSVSerializer()
        max_limit=0
        authentication = ApiKeyAuthentication()

class SpecimenResource(ModelResource):
    museum = fields.ForeignKey(MuseumResource, "museum", full=True, null=True, blank=True)
    collection = fields.ForeignKey(CollectionResource, "collection",full=True, null=True, blank=True)
    taxon = fields.ForeignKey(TaxonomyResource, attribute="taxon", null=True, blank=True, full=True) #attribute is the name of the related field in model (not resource)
    #measurements = fields.ToManyField("API.API_resources.MeasurementResource","measurement_set", related_name="specimen")
    class Meta:
        queryset = specimen.objects.all()
        allowed_methods=['get']
        fields = ["anatomicalElement", "description", "id", "localityNumber", "localityPrefix", "pathology", "sex", "specimenNumber"]
        resource_name = 'specimen'
        serializer = CSVSerializer()
        max_limit=0
        authentication = ApiKeyAuthentication()
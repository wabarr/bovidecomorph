from bovidecoapp.models import *
from django.contrib import admin


class measurementInline(admin.TabularInline):
	model = measurement
	extra = 10
class observationInline(admin.TabularInline):
	model = observation
	extra = 3


class MetricCharacterAdmin(admin.ModelAdmin):
	list_display = ("code","element","name","method","ref","active")
	list_filter = ['element','method','ref','active']
	search_fields = ['name']
	
class NonMetricCharacterAdmin(admin.ModelAdmin):
	list_display = ("code","element","name","method","ref")
	list_filter = ['element','method','ref']
	search_fields = ['name']
	
class specimenAdmin(admin.ModelAdmin):
	#long list display below
	list_display = ("specimenNumber","display_add_data_link","specimen_Collection_Information","taxon","anatomicalElement","astragScanned","ASCII_Trim","ROUGHORIENT","ORIENTED","linearMeasurements","description","analyticalUnit","sex",)
	list_editable = ["anatomicalElement","astragScanned","ASCII_Trim","ROUGHORIENT","ORIENTED","linearMeasurements","sex","description"]

		
	#short list display below
	#list_display = ("museum","catalogNumberSearchString","barcode","analyticalUnit","anatomicalElement","Mesowear","astragScanned","mesoUpperOrLower","taxon","pathology","sex")

	#long list filters
	list_filter = ["astragScanned","museum","ASCII_Trim","sex","ROUGHORIENT","ORIENTED","linearMeasurements","HRPCFcomplete","GISMeasurementsDone"]
	
	#short list filters
	list_filter = ["astragScanned","museum","Mesowear","collection","analyticalUnit"]

	inlines = [measurementInline,observationInline]
	#note the below works based on the foreignkey__relatedField 'follow' syntax
	search_fields = ["taxon__genusName","taxon__specificEpithet","taxon__commonName","catalogNumberSearchString","barcode","specimenNumber"]
	
	fieldsets = (
		('Curation', {
		    'fields': (('museum', 'collection','localityPrefix','localityNumber','specimenNumber','specimenPart','analyticalUnit','anatomicalElement','description'),)
		}),
		('Specimen', {
		    'fields': (('taxon','pathology','sex'),)
		}),
		('Scanning', {
		    'fields': (("astragScanned","ASCII_Trim","ROUGHORIENT","ORIENTED","linearMeasurements","visiblePointsExported","GISMeasurementsDone"),)
		}),
		('Mesowear', {
		    'fields': (("mesoUpperOrLower"),)
		}),
		
	    )

class museumAdmin(admin.ModelAdmin):
	list_display = ("code","contactName","contactEmail")
	
class taxonomyAdmin(admin.ModelAdmin):
	list_display = ("order","extant","family","subFamily","tribe","genusName","specificEpithet","infraspecificEpithet","commonName","taxonRank","Fernandez_Vrba_2005_Name","BinindaEmonds_2008_Name")
	list_filter = ['taxonRank','extant']
	list_editable = ['extant','tribe']
	search_fields = ['family','subFamily','tribe','genusName','specificEpithet','synonyms']
	fieldsets = (
		('', {
		    'fields': (("taxonRank","extant"),)
		}),
		('', {
		    'fields': (("order","family","subFamily","tribe"),)
		}),
		('', {
		    'fields': (("genusName","specificEpithet","infraspecificEpithet"),)
		}),
		('', {
		    'fields': (("commonName","Fernandez_Vrba_2005_Name","BinindaEmonds_2008_Name"),)
		}),
		('', {
		    'fields': (("synonyms","ref"),)
		}),
	    )
	
class collectionAdmin(admin.ModelAdmin):
	list_display = ("museum","code","name")
	
class measurementAdmin(admin.ModelAdmin):
	list_display = ("MetricCharacter","specimen","value")
	search_fields = ['specimen__museum__code','specimen__specimenNumber']
	list_filter = ["MetricCharacter"]
	list_editable = ["value"]
	
class observationAdmin(admin.ModelAdmin):
	list_display = ("NonMetricCharacter","specimen","value")
	list_filter = ["NonMetricCharacter"]
	search_fields = ["specimen__specimenNumber","specimen__collection"]
	list_editable = ["value"]
	
class Kapp1991HabitatAdmin(admin.ModelAdmin):
	list_display = ("taxon","habitat","verbatimTaxon")
	list_filter = ['habitat']
	search_fields = ['taxon__genusName','taxon__specificEpithet']

class Kapp1997HabitatAdmin(admin.ModelAdmin):
	list_display = ("taxon","habitat","verbatimTaxon")
	list_filter = ['habitat']
	search_fields = ['taxon__genusName','taxon__specificEpithet']

class PlummerBishop2008HabitatAdmin(admin.ModelAdmin):
	list_display = ("taxon","habitat","verbatimTaxon")
	list_filter = ['habitat']
	search_fields = ['taxon__genusName','taxon__specificEpithet']

class HabitatAdmin(admin.ModelAdmin):
	list_display = ("taxon","habitat","ref")
	list_filter = ['habitat']
	search_fields = ['taxon__genusName','taxon__specificEpithet']
	
class RobScottHabitatAdmin(admin.ModelAdmin):
	list_display = ("taxon","habitat")
	list_filter = ['habitat']
	search_fields = ['taxon__genusName','taxon__specificEpithet']
	
class KovarovicAndrews2007HabitatAdmin(admin.ModelAdmin):
	list_display = ("taxon","habitat","verbatimTaxon")
	list_filter = ['habitat']
	search_fields = ['taxon__genusName','taxon__specificEpithet']

class allAmnhBovidAdmin(admin.ModelAdmin):
	list_display = ("catalogNum","identification","sex","preps")
	list_filter = ['sex',"preps"]
	search_fields = ["identification","catalogNum"]
	
class PantheriaBodyMassAdmin(admin.ModelAdmin):
	list_display = ("taxon","bodyMassGrams")
	list_editable = ["bodyMassGrams"]
class ForteliusSolouniasAdmin(admin.ModelAdmin):
	list_display = ("taxon","adhoc_class","n","cons","radi","jad1","hyp_ind","perhigh","persharp","perround","perblunt","AfricanBovid")

admin.site.register(ForteliusSolouniasTable1,ForteliusSolouniasAdmin)
admin.site.register(MetricCharacter,MetricCharacterAdmin)
admin.site.register(NonMetricCharacter,NonMetricCharacterAdmin)
admin.site.register(reference)
admin.site.register(taxonomy,taxonomyAdmin)
admin.site.register(museum, museumAdmin)
admin.site.register(collection,collectionAdmin)
admin.site.register(Habitat,HabitatAdmin)
admin.site.register(RobScottHabitat,RobScottHabitatAdmin)
admin.site.register(specimen,specimenAdmin)
admin.site.register(measurement,measurementAdmin)
admin.site.register(observation,observationAdmin)
admin.site.register(Kapp1991Habitat,Kapp1991HabitatAdmin)
admin.site.register(Kapp1997Habitat,Kapp1997HabitatAdmin)
admin.site.register(PlummerBishop2008Habitat,PlummerBishop2008HabitatAdmin)
admin.site.register(KovarovicAndrews2007Habitat,KovarovicAndrews2007HabitatAdmin)
admin.site.register(allAmnhBovid,allAmnhBovidAdmin)
admin.site.register(PantheriaBodyMass,PantheriaBodyMassAdmin)

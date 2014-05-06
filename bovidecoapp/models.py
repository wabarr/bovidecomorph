from django.db import models

class reference(models.Model):
    authorshortstring = models.CharField(max_length = 100)
    year = models.IntegerField()
    def __unicode__(self):
    	    name = self.authorshortstring + ", " + str(self.year)
    	    return name
    class Meta:
    	    db_table = 'reference'

##choices for upcoming taxonomy class
CHOICES_KINGDOM = (
	("Animalia","Animalia"),
)

CHOICES_PHYLUM = (
	("Chordata","Chordata"),
)

CHOICES_CLASS = (
	("Mammalia","Mammalia"),
	("Reptilia","Reptilia"),
	("Pisces","Pisces"),
	("Aves","Aves"),
	("Amphibia","Amphibia"),
)

CHOICES_ORDER = (
	("ARTIODACTYLA","ARTIODACTYLA"),
	("CARNIVORA","CARNIVORA"),
	("PERISSODACTYLA","PERISSODACTYLA"),
	("PRIMATES","PRIMATES"),
	("PROBOSCIDEA","PROBOSCIDEA"),
	("RODENTIA","RODENTIA"),
	("AFROSORICIDA","AFROSORICIDA"),
	("CETACEA","CETACEA"),
	("CHIROPTERA","CHIROPTERA"),
	("CINGULATA","CINGULATA"),
	("DASYUROMORPHIA","DASYUROMORPHIA"),
	("DERMOPTERA","DERMOPTERA"),
	("DIDELPHIMORPHIA","DIDELPHIMORPHIA"),
	("DIPROTODONTIA","DIPROTODONTIA"),
	("ERINACEOMORPHA","ERINACEOMORPHA"),
	("HYRACOIDEA","HYRACOIDEA"),
	("LAGOMORPHA","LAGOMORPHA"),
	("MACROSCELIDEA","MACROSCELIDEA"),
	("MICROBIOTHERIA","MICROBIOTHERIA"),
	("MONOTREMATA","MONOTREMATA"),
	("NOTORYCTEMORPHIA","NOTORYCTEMORPHIA"),
	("PAUCITUBERCULATA","PAUCITUBERCULATA"),
	("PERAMELEMORPHIA","PERAMELEMORPHIA"),
	("PHOLIDOTA","PHOLIDOTA"),
	("PILOSA","PILOSA"),
	("SCANDENTIA","SCANDENTIA"),
	("SIRENIA","SIRENIA"),
	("SORICOMORPHA","SORICOMORPHA"),
	("TUBULIDENTATA","TUBULIDENTATA"),

)

CHOICES_RANK=(
	('CLASS','CLASS'),
	('ORDER','ORDER'),
	('FAMILY','FAMILY'),
	('SUBFAMILY','SUBFAMILY'),
	('TRIBE','TRIBE'),
	('GENUS','GENUS'),
	('SPECIES','SPECIES'),
	('SUBSPECIES','SUBSPECIES'),
	('INFRAORDER','INFRAORDER'),
	('SUBGENUS','SUBGENUS'),
	('SUBORDER','SUBORDER'),
	('SUPERFAMILY','SUPERFAMILY'),
)

class taxonomy(models.Model):
	kingdom = models.CharField(max_length=100, null=True, blank=True, choices = CHOICES_KINGDOM, default="Animalia")
	phylum = models.CharField(max_length=100, null=True, blank=True, choices = CHOICES_PHYLUM, default = "Chordata")
	tclass = models.CharField(max_length=100, null=True, blank=True, choices = CHOICES_CLASS)
	order = models.CharField(max_length=100, null=True, blank=True, choices = CHOICES_ORDER)
	family = models.CharField(max_length=100, null=True, blank=True)
	subFamily = models.CharField(max_length=100, null=True, blank=True)
	tribe = models.CharField(max_length=100, null=True, blank=True)
	genusName = models.CharField(max_length=100, null=True, blank=True)
	specificEpithet = models.CharField(max_length=100, null=True, blank=True)
	infraspecificEpithet = models.CharField(max_length=100, null=True, blank=True)
	identificationQualifier = models.CharField(max_length=100, null=True, blank=True)
	extant = models.BooleanField()
	commonName = models.CharField(max_length=100, null=True, blank=True)
	synonyms = models.CharField(max_length=2000, null=True, blank=True)
	taxonRank = models.CharField(max_length=100, null=True, blank=False, choices=CHOICES_RANK)
	ref = models.ForeignKey(reference)
	Fernandez_Vrba_2005_Name = models.CharField(max_length=255, null=True, blank=True)
	BinindaEmonds_2008_Name = models.CharField(max_length=255, null=True, blank=True)

	def __unicode__(self):
		if str(self.taxonRank).lower() == 'class':
			return self.tclass
		elif str(self.taxonRank).lower() == 'order':
			return self.order
		elif str(self.taxonRank).lower() == 'family':
			return self.family
		elif str(self.taxonRank).lower() == 'subfamily':
			return self.subFamily
		elif str(self.taxonRank).lower() == 'tribe':
			return self.tribe
		elif str(self.taxonRank).lower() == 'genus':
			return self.genusName
		elif str(self.taxonRank).lower() == 'species':
			return self.genusName + " " + self.specificEpithet + "  (" + self.commonName + ")"
		elif str(self.taxonRank).lower() == 'subspecies':
			return self.genusName + " " + self.specificEpithet + " " + self.infraspecificEpithet + "  (" + self.commonName  + ")"
		else:
			return " "
	class Meta:
		db_table = 'taxonomy'

class museum(models.Model):
	code = models.CharField(max_length=10)
	name = models.CharField(max_length=50)
	contactName = models.CharField(max_length=50,blank="True")
	contactEmail = models.EmailField(blank="True")
	contactPhone = models.CharField(max_length=15,blank="True")
	def __unicode__(self):
		return self.code
	class Meta:
		db_table = 'museum'

class collection(models.Model):
	museum = models.ForeignKey(museum)
	code = models.CharField(max_length = 10)
	name = models.CharField(max_length = 20)
	class Meta:
		db_table = 'collection'

	def __unicode__(self):
		return self.code


anatomicalElementChoices = (
	("M1/2","M1/2"),
	("m3","m3"),
	("m1/2","m1/2"),
	("M3","M3"),
	("unspecifiedMolar","unspecifiedMolar"),
	("astragalus","astragalus"),
	("skeleton","skeleton"),
	("mandible","mandible"),
	("maxilla","maxilla"),
)

class specimen(models.Model):
    taxon = models.ForeignKey(taxonomy)
    museum = models.ForeignKey(museum, default=3)
    collection = models.ForeignKey(collection,default=4)
    localityPrefix = models.CharField(max_length=5,blank="True")
    localityNumber = models.IntegerField(default=-999)
    specimenNumber = models.IntegerField()
    specimenPart = models.CharField(max_length=3,blank="True")
    catalogNumberSearchString = models.CharField(max_length=100,blank="True")
    barcode = models.IntegerField(blank="True")
    analyticalUnit = models.CharField(max_length=100,blank="True")
    description = models.CharField(max_length = 100)
    anatomicalElement = models.CharField(max_length = 100,choices=anatomicalElementChoices,default="astragalus")
    pathology = models.CharField(max_length = 255,blank="True")
    astragScanned = models.BooleanField()
    Mesowear = models.BooleanField()
    mesoUpperOrLower = models.CharField(max_length = 10,blank=True,choices=(('upper','upper'),('lower','lower')))
    scanFilePath = models.CharField(max_length = 255,blank="True")
    sex = models.CharField(max_length=10,blank=True,choices=(('male','male'),('female','female'),('sex_unk','sexUnknown')))
    ASCII_Trim = models.BooleanField()
    ROUGHORIENT = models.BooleanField()
    ORIENTED = models.BooleanField()
    linearMeasurements = models.BooleanField()
    HRPCFoutlinesCreated = models.BooleanField()
    HRPCFcomplete = models.BooleanField()
    visiblePointsExported = models.BooleanField()
    GISMeasurementsDone = models.BooleanField()

    def __unicode__(self):
        return str(self.museum) + "-" + str(self.collection) + "-" + str(self.localityNumber) + "-" +  str(self.specimenNumber) + " [" + str(self.taxon) + "]"

    def display_add_data_link(self):
        return '<a href="%s">Take Measurements</a>' % ("/add_data/" + str(self.id))
    display_add_data_link.allow_tags = True

    def specimen_Collection_Information(self):
        if str(self.collection) == 'FREN-OMO':
            return str(self.localityPrefix) + '-' + str(self.localityNumber) + "-" +  str(self.specimenNumber) + str(self.specimenPart)
        else:
            return str(self.collection) + '-' + str(self.localityPrefix) + str(self.localityNumber) + "-" +  str(self.specimenNumber) + str(self.specimenPart)

    class Meta:
        db_table = 'specimen'


##Choices for upcoming character class                                
ELEMENT_CHOICES = (
        ('Astragalus','Astragalus'),
        ("Distal Femur","Distal Femur"),
        ("Femur","Femur"),
        ("Metacarpal","Metacarpal"),
        ("Metapodials","Metapodials"),
        ("Metatarsal","Metatarsal"),
        ("Molar","Molar"),
        ("Proximal Femur","Proximal Femur"),
        ("Tibia","Tibia"),
)

METHOD_CHOICES = (
	('OB','Osteometric Board'),
	('PH','Photographic'),
	('CA','Caliper'),
	('HRPCF','HRPCF'),
	('ML','MeshLab'),
	('VIS','VisualObservation'),
	('DER','Derived')
)


class MetricCharacter(models.Model):
	element = models.CharField(max_length = 25, choices = ELEMENT_CHOICES, default = "Astragalus")
	code = models.CharField(max_length = 10, unique = "TRUE")
	name = models.CharField(max_length = 255)
	description = models.CharField(max_length = 500)
	method = models.CharField(max_length = 20, choices = METHOD_CHOICES)
	ref = models.ForeignKey(reference)

	def __unicode__(self):
		return self.code

	class Meta:
		db_table = 'MetricCharacter'
		ordering = ['code']

class measurement(models.Model):
	MetricCharacter = models.ForeignKey(MetricCharacter)
	specimen = models.ForeignKey(specimen)
	value = models.DecimalField(max_digits = 10, decimal_places = 5)
	comments = models.CharField(max_length = 100,blank="True")
	class Meta:
		db_table = 'measurement'
		unique_together = (("specimen", "MetricCharacter"),)


class NonMetricCharacter(models.Model):
	element = models.CharField(max_length = 25, choices = ELEMENT_CHOICES, default = "Astragalus")
	code = models.CharField(max_length = 10, unique = "TRUE")
	name = models.CharField(max_length = 255)
	description = models.CharField(max_length = 500)
	method = models.CharField(max_length = 20, choices = METHOD_CHOICES)
	ref = models.ForeignKey(reference)

	def __unicode__(self):
		return self.code

	class Meta:
		db_table = 'NonMetricCharacter'

CUSP_RELIEF_CHOICES=(
	("Sharp","Sharp"),
	("Round","Round"),
	("Blunt","Blunt"),
	("High","HighRelief"),
	("Low","LowRelief")

	)

class observation(models.Model):
	NonMetricCharacter = models.ForeignKey(NonMetricCharacter)
	specimen = models.ForeignKey(specimen)
	value = models.CharField(max_length=10,choices=CUSP_RELIEF_CHOICES)
	comments = models.CharField(max_length = 100,blank="True")
	class Meta:
		db_table = 'nonMetricObservation'




CHOICES_KAPP1991HAB=(
	('Closed','Closed'),
	('Intermediate','Intermediate'),
	('Open','Open'),
)

class Kapp1991Habitat(models.Model):
	taxon = models.ForeignKey(taxonomy)
	habitat = models.CharField(max_length = 15, blank="True", null="True", choices=CHOICES_KAPP1991HAB)
	verbatimTaxon = models.CharField(max_length = 255, blank="True", null="True")
	class Meta:
		db_table = 'Kapp1991Habitat'

CHOICES_ROBSCOTTHAB=(
	('Plains','Plains'),
	('LightCover','LightCover'),
	('HeavyCover','HeavyCover'),
	('Forest','Forest'),
	('Mountain','Mountain')
)

class RobScottHabitat(models.Model):
	taxon = models.ForeignKey(taxonomy)
	habitat = models.CharField(max_length = 15, blank="True", null="True", choices=CHOICES_ROBSCOTTHAB)
	verbatimTaxon = models.CharField(max_length = 255, blank="True", null="True")
	class Meta:
		db_table = 'RobScottHabitat'



CHOICES_PLUMMERBISHOP2008HAB=(
	('Forest','Forest'),
	('HeavyCover','HeavyCover'),
	('LightCover','LightCover'),
	('Open','Open')
)

class Kapp1997Habitat(models.Model):
	taxon = models.ForeignKey(taxonomy)
	habitat = models.CharField(max_length = 15, blank="True", null="True", choices=CHOICES_PLUMMERBISHOP2008HAB)
	verbatimTaxon = models.CharField(max_length = 255, blank="True", null="True")
	class Meta:
		db_table = 'Kapp1997Habitat'

class PlummerBishop2008Habitat(models.Model):
	taxon = models.ForeignKey(taxonomy)
	habitat = models.CharField(max_length = 15, blank="True", null="True", choices=CHOICES_PLUMMERBISHOP2008HAB)
	verbatimTaxon = models.CharField(max_length = 255, blank="True", null="True")
	class Meta:
		db_table = 'PlummerBishop2008Habitat'

class Habitat(models.Model):
	taxon = models.ForeignKey(taxonomy)
	habitat = models.CharField(max_length = 15, blank="True", null="True", choices=CHOICES_PLUMMERBISHOP2008HAB)
	verbatimTaxon = models.CharField(max_length = 255, blank="True", null="True")
	ref = models.ForeignKey(reference)
	class Meta:
		db_table = 'Habitat'

CHOICES_KOVAROVICANDREWS2007HAB=(
	('Grassland','Grassland'),
	('WoodedBushedGrassland','WoodedBushedGrassland'),
	('LightWoodlandBushland','LightWoodlandBushland'),
	('HeavyWoodlandBushland','HeavyWoodlandBushland'),
	('Forest','Forest'),
	('MontaneLightCover','MontaneLightCover'),
	('MontaneHeavyCover','MontaneHeavyCover')
)

class KovarovicAndrews2007Habitat(models.Model):
	taxon = models.ForeignKey(taxonomy)
	habitat = models.CharField(max_length = 30, blank="True", null="True", choices=CHOICES_KOVAROVICANDREWS2007HAB)
	verbatimTaxon = models.CharField(max_length = 255, blank="True", null="True")
	class Meta:
		db_table = 'KovarovicAndrews2007Habitat'


class allAmnhBovid(models.Model):
	collectionCode = models.CharField(max_length=10)
	catalogNum = models.IntegerField()
	identification = models.CharField(max_length=100,blank="True",null="True")
	country = models.CharField(max_length=100,blank="True",null="True")
	state = models.CharField(max_length=100,blank="True",null="True")
	county = models.CharField(max_length=100,blank="True",null="True")
	precise_locality = models.CharField(max_length=100,blank="True",null="True")
	collector = models.CharField(max_length=100,blank="True",null="True")
	collection_date = models.CharField(max_length=100,blank="True",null="True")
	preps = models.CharField(max_length=100,blank="True",null="True")
	sex = models.CharField(max_length=10,choices=(('male','male'),('female','female'),('unknown','unknown')))
	class Meta:
		db_table = 'allAmnhBovid'
	def __unicode__(self):
		return str(self.collectionCode) + "-" + str(self.catalogNum) + "(" + str(self.identification) + ")"

class PantheriaBodyMass(models.Model):
	taxon = models.ForeignKey(taxonomy)
	bodyMassGrams = models.IntegerField(blank="True",null="True")
	class Meta:
		db_table = "PantheriaBodyMass"

class ForteliusSolouniasTable1(models.Model):
	taxon = models.ForeignKey(taxonomy)
	adhoc_class = models.CharField(max_length=100,blank="True",null="True")
	n = models.IntegerField(blank="True",null="True")
	cons =  models.CharField(max_length=100,blank="True",null="True")
	radi = models.CharField(max_length=100,blank="True",null="True")
	jad1 = models.CharField(max_length=100,blank="True",null="True")
	hyp_ind = models.DecimalField(max_digits = 10, decimal_places = 5,blank="True",null="True")
	perhigh = models.DecimalField(max_digits = 10, decimal_places = 5,blank="True",null="True")
	persharp = models.DecimalField(max_digits = 10, decimal_places = 5,blank="True",null="True")
	perround = models.DecimalField(max_digits = 10, decimal_places = 5,blank="True",null="True")
	perblunt = models.DecimalField(max_digits = 10, decimal_places = 5,blank="True",null="True")
	##whether not an African bovid for inclusion in comparative sample
	AfricanBovid = models.CharField(max_length=100,blank="True",null="True")
	class Meta:
		db_table = "ForteliusSolounias"



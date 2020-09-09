from django.db import models, connection
from django.utils import timezone 

class Covid(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.TextField(max_length=255, null=True)
    cases = models.BigIntegerField(null=True)
    todayCases = models.BigIntegerField(null=True)
    deaths = models.BigIntegerField(null=True)
    todayDeaths = models.BigIntegerField(null=True)
    recovered = models.BigIntegerField(null=True)
    active = models.BigIntegerField(null=True)
    critical = models.BigIntegerField(null=True)
    casesPerOneMillion = models.BigIntegerField(null=True)
    deathsPerOneMillion = models.BigIntegerField(null=True)
    totalTests = models.BigIntegerField(null=True)
    testsPerOneMillion = models.BigIntegerField(null=True)
    updated_date = models.DateTimeField(default=timezone.now) 

    def __str__(self): 
        return self.country 

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE %s ' % (cls._meta.db_table))

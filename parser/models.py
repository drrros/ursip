from django.db import models


class CompanyData(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    fact_qliq_data1 = models.FloatField()
    fact_qliq_data2 = models.FloatField()
    fact_qoil_data1 = models.FloatField()
    fact_qoil_data2 = models.FloatField()
    forecast_qliq_data1 = models.FloatField()
    forecast_qliq_data2 = models.FloatField()
    forecast_qoil_data1 = models.FloatField()
    forecast_qoil_data2 = models.FloatField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.company

    @staticmethod
    def get_fields():
        for field in CompanyData._meta.get_fields():
            yield field

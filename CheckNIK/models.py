from django import db
from django.db import models

class Dukcapilmodel(models.Model):
    m_dukcapil_data_id = models.AutoField(auto_created=True, primary_key=True) 
    nik = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    maiden_name = models.CharField(max_length=10)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1)
    religion_id = models.IntegerField()
    marital_status = models.IntegerField()
    class Meta:
        db_table='m_dukcapil_data'

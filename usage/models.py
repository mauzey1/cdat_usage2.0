from django.db import models
from datetime import datetime

# Create your models here.
class Entry(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    
    platform = models.CharField(max_length=1024, blank=True, null=False)
    platform_version = models.CharField(max_length=1024, blank=True, null=False)
    hashed_hostname = models.CharField(max_length=1024, blank=True, null=False)
    source = models.CharField(max_length=1024, blank=True, null=False)
    cdat_info_version = models.CharField(max_length=1024, blank=True, null=False)
    source_version = models.CharField(max_length=1024, blank=True, null=False)
    action = models.CharField(max_length=1024, blank=True, null=False)
    sleep = models.CharField(max_length=1024, blank=True, null=False)
    pid = models.CharField(max_length=1024, blank=True, null=False)
    hashed_username = models.CharField(max_length=1024, blank=True, null=False)
    gmtime = models.DateTimeField(default=datetime.now, blank=True, null=False)
    ip = models.GenericIPAddressField(null=False, blank=False)
    domain = models.CharField(max_length=1024, blank=True, null=False)

    date = models.DateTimeField(default=datetime.now, blank=True, null=False)

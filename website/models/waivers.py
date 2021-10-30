from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from datetime import timedelta
from website.models.user import User

class Waiver(models.Model):
    waiver = models.FileField(null = True, blank = True)
    user = models.OneToOneField(User, related_name = "waiver", on_delete=models.CASCADE)
    

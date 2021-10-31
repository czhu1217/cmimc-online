from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from datetime import timedelta
from website.models.user import User
from website.utils import get_file_path

class Waiver(models.Model):
    waiver = models.FileField(null = True, blank = True, upload_to=get_file_path)
    time_submitted = models.TimeField(null=True, auto_now_add=True)
    user = models.OneToOneField(User, related_name = "waiver", on_delete=models.CASCADE)
    class Meta:
        db_table = "waiver"

    def __str__(self):
        return "Waiver: {0}".format(self.user.name)

   

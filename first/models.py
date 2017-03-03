from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SignUp(models.Model):
	email=models.EmailField(null=True,blank=True)
	full_name=models.CharField(max_length=120,null=True,blank=True)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	updated=models.DateTimeField(auto_now_add=False,auto_now=True)

	def __unicode__(self):  # Python 3.3 is __str__
		return self.email
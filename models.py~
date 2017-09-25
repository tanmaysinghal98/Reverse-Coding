from django.db import models
from django.contrib.auth.models import User

class Players(models.Model):
	pname1=models.CharField(max_length=100,blank = True,null=True)
	phone1=models.CharField(max_length=100, blank=False,null=False)
	email1=models.EmailField(max_length=100,blank=False,null=False)
	pname2=models.CharField(max_length=100)
	phone2=models.CharField(max_length=100)
	email2=models.EmailField(max_length=100)
	total_score = models.IntegerField(default = 0)
	count=models.IntegerField(default = 2)
	user=models.OneToOneField(User,null=True,blank=True)
	start_time=models.IntegerField(default = 0)
	end_time=models.IntegerField(default = 0)
	marking=models.IntegerField(default = 4)
	previous_answer=models.CharField(max_length=100)
	questions_attempted=models.IntegerField(default=0)
	right_count=models.IntegerField(default=0)
	wrong_count=models.IntegerField(default=0)  
##############################################################################################################
class Question(models.Model):
	question=models.TextField(max_length = 1000000)
	correct_option=models.CharField(max_length = 100)   #Doubt
	#level = models.IntegerField(default = 0)#0 for junior 1 for senior

class Qattempt(models.Model):
	user = models.ForeignKey(User)
	question = models.ForeignKey(Question)    
#############################################################################################################



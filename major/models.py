from django.db import models

# Create your models here.
class IT(models.Model):
	dept = models.CharField(max_length=255)
	dept_phone = models.CharField(max_length=11)
	people = models.CharField(max_length=255)
	teachers = models.CharField(max_length=255)
	a_chaw_sone = models.CharField(max_length=255)

class EC(models.Model):
	dept = models.CharField(max_length=255)
	dept_phone = models.CharField(max_length=11)
	people = models.CharField(max_length=255)
	teachers = models.CharField(max_length=255)
	a_chaw_sone = models.CharField(max_length=255)

class MC(models.Model):
	dept = models.CharField(max_length=255)
	dept_phone = models.CharField(max_length=11)
	people = models.CharField(max_length=255)
	teachers = models.CharField(max_length=255)
	a_chaw_sone = models.CharField(max_length=255)

class chE(models.Model):
	dept = models.CharField(max_length=255)
	dept_phone = models.CharField(max_length=11)
	people = models.CharField(max_length=255)
	teachers = models.CharField(max_length=255)
	a_chaw_sone = models.CharField(max_length=255)

class mech(models.Model):
	dept = models.CharField(max_length=255)
	dept_phone = models.CharField(max_length=11)
	people = models.CharField(max_length=255)
	teachers = models.CharField(max_length=255)
	a_chaw_sone = models.CharField(max_length=255)

# class civil(models.Model):
# 	dept = models.CharField(max_length=255)
# 	dept_phone = models.CharField(max_length=11)
# 	people = models.DecimalField(decimal_places=4)
# 	teachers = models.DecimalField(decimal_places=4)
# 	a_chaw_sone = models.CharField(max_length=255)

# class petrol(models.Model):
# 	dept = models.CharField(max_length=255)
# 	dept_phone = models.CharField(max_length=11)
# 	people = models.DecimalField(decimal_places=4)
# 	teachers = models.DecimalField(decimal_places=4)
# 	a_chaw_sone = models.CharField(max_length=255)

# class EP(models.Model):
# 	dept = models.CharField(max_length=255)
# 	dept_phone = models.CharField(max_length=11)
# 	people = models.DecimalField(decimal_places=4)
# 	teachers = models.DecimalField(decimal_places=4)
# 	a_chaw_sone = models.CharField(max_length=255)

# class arch(models.Model):
# 	dept = models.CharField(max_length=255)
# 	dept_phone = models.CharField(max_length=11)
# 	people = models.DecimalField(decimal_places=4)
# 	teachers = models.DecimalField(decimal_places=4)
# 	a_chaw_sone = models.CharField(max_length=255)
from django.db import models

class Scholar(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=150,null=False,blank=False)
    email = models.EmailField(null=False) 
    secemail = models.EmailField(null=False)
    number = models.DecimalField(max_digits=10, decimal_places=0)
    address = models.TextField(max_length=300,null=False,blank=False)
    collegename = models.CharField(max_length=150,null=False,blank=False)
    grno = models.DecimalField(max_digits=10, decimal_places=0)
    marksheet = models.FileField(upload_to='schloar_marksheet/',null=False, blank=False)
    feereceipt = models.FileField(upload_to='schloar_feereceipt/',null=False, blank=False)

    def _str_(self):
        return str(self.fullname)

class counselor(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=150,null=False,blank=False)
    number = models.DecimalField(max_digits=10, decimal_places=0)
    course = models.CharField(max_length=100,null=False,blank=False)
    proof = models.FileField(upload_to='course_proof/',null=False, blank=False)
    address = models.TextField(max_length=300,null=False,blank=False)
    email = models.EmailField(null=False ,blank=False)

    def _str_(self):
        return str(self.email)
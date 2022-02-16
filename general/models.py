from django.db import models

class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=150,null=False,blank=False)
    email = models.EmailField(null=False ,blank=False)
    feedback = models.TextField(null=False,blank=False)
    
    def _str_(self):
        return str(self.email)
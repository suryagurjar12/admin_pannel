from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Contect=models.IntegerField()
    City=models.CharField(max_length=50)
    
    def __str__(self):
        return self.Name+' '+self.Email+' '+self.City
    
    class Meta:
        db_table="Student"
        
        #admin pennel pr name change krna lekin name ke last mai s nhi htega
        verbose_name='student' 
        
        #isme name chage bhi hoga or s bhi hat jaega
        verbose_name_plural='Student1234'
        
        #order change kr skte hai assending oder and desending oder
        ordering=['Name']

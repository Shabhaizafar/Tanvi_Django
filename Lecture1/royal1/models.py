from django.db import models

# Create your models here.

class Royal(models.Model):
    fname = models.CharField(max_length=255)
    age = models.IntegerField(max_length=100)
    lname = models.CharField(null=True)

'''
[ 
{'id': 1, 'fname': 'Raj', 'age': 28}, 
{'id': 2, 'fname': 'Ajay', 'age': 29}, 
{'id': 3, 'fname': 'Rajesh', 'age': 40}, 
{'id': 4, 'fname': 'Vivek', 'age': 21}, 
{'id': 5, 'fname': 'Rajesh', 'age': 30}
]
'''
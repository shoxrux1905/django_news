from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class New(models.Model) :
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='news')
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True, related_name='news')
    
    def __str__(self):
        return self.title


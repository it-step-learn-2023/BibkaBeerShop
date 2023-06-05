from django.db import models

# Create your models here.
class Category(models.Model):
    # Props
    name = models.CharField(max_length=100, unique=True)
    
    # Presintation
    def __str__(self) -> str:
        return str(self.name)
    
class Producer(models.Model):
    # Props
    name = models.CharField(max_length=100, unique=True)
    
    # Presintation
    def __str__(self) -> str:
        return str(self.name)
    
class Product(models.Model):
    # Props
    name = models.CharField(max_length=100, unique=True)
    about = models.TextField(max_length=500, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    photo = models.FileField(upload_to='products/')
    quantitiy = models.IntegerField(default=1)
    displacement = models.FloatField(max_length=50,  default=0.5)
    price = models.FloatField()
    sales = models.IntegerField(default=0)
    rate = models.FloatField(max_length=50, default=5)
    
    # Presintation
    def __str__(self) -> str:
        return str(self.name)
    
class Coment(models.Model):
    # props
    name = models.CharField(max_length=100)
    coment_text = models.TextField(max_length=500)
    rate = models.IntegerField(default=1)
    date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # Presintation
    def __str__(self) -> str:
        return str(self.name)

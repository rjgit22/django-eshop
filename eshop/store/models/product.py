from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    categories = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
       return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_Categoryid(category_id):
        if category_id:
             return Product.objects.filter(categories = category_id);
        else:
            return Product.get_all_products();
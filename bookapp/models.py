from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=255)
    book_author = models.CharField(max_length=200)
    book_description = models.CharField(max_length=255)
    book_category = models.CharField(max_length=100)
    book_price = models.IntegerField()
    book_image = models.ImageField(upload_to='images/')
    book_pages = models.IntegerField()
    book_copies = models.IntegerField()
    book_publisher = models.CharField(max_length=200)

    class Meta:
        db_table = "book"

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)

    class Meta:
        db_table = "cart"
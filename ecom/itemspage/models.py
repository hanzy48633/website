from django.db import models


CATEGORY_CHOICES = (
    ('FR', 'Fruit'),
    ('VG', 'Vegetable'),
    ('GR', 'Grocery Item'),
    ('MT', 'Meat'),
)

PRICE_CATEGORY = (
    ('PP', 'per piece'),
    ('PK', 'per Kg')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    price_type = models.CharField(choices=PRICE_CATEGORY, max_length=2, default='PP')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    quantity = models.IntegerField()
    description = models.TextField(default="This is the description for the {}".format(title))
    desc = models.CharField(max_length=1000, default="This is the description for the {}".format(title))
    image = models.ImageField()

    def __str__(self):
        return self.title


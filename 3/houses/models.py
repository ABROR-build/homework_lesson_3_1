from django.db import models


class SalesTypes(models.Model):
    type = models.CharField(max_length=300)

    class Meta:
        db_table = 'SalesTypes'

    def __str__(self):
        return self.type


class ForRent(models.Model):
    type = models.ForeignKey(SalesTypes, on_delete=models.CASCADE)
    house_type = models.CharField(max_length=300)
    rent_per_month = models.FloatField()
    comments = models.TextField()

    class Meta:
        db_table = 'ForRent'

    def __str__(self):
        return f"{self.type} {self.house_type}"


class ForSale(models.Model):
    type = models.ForeignKey(SalesTypes, on_delete=models.CASCADE)
    house_type = models.CharField(max_length=300)
    price = models.FloatField()
    comments = models.TextField()

    class Meta:
        db_table = 'ForSale'

    def __str__(self):
        return f"{self.type} {self.house_type}"

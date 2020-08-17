from django.db import models


class Pianos(models.Model):
    id = models.AutoField(primary_key=True, db_column="rowid")
    title = models.CharField(max_length=100, db_column="title")
    image_url = models.URLField(db_column="image_url")
    description = models.TextField(db_column="description")
    price = models.CharField(max_length=100, db_column="price")
    length = models.CharField(max_length=100, db_column="length")

    class Meta:
        db_table = "pianos"

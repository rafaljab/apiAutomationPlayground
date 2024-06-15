from django.db import models


def product_path(instance: "Product", filename: str):
    extension = filename.split(".")[-1]
    name = instance.title.lower().replace(" ", "_")
    new_filename = ".".join([name, extension])
    return "/".join(["shop/products", new_filename])


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to=product_path)

    def __str__(self):
        return self.title

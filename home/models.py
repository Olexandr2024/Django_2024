from django.db import models

# Create your models here.


class Category(models.Model):
    slug = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, unique=True)

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    sreated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __iter__(self):
        dishes = self.dishes.filter(is_visible=True).order_by("sort")
        for dish in dishes:
            yield dish

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.IntegerField()
    unit = models.CharField(max_length=10)

    photo = models.ImageField(upload_to="dishes", blank=True, null=True)

    is_available = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)
    sreated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="dishes"
    )

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()

    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    organizer = models.CharField(max_length=100)

    banner = models.ImageField(upload_to="events", blank=True, null=True)

    is_active = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Chef(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    experience_years = models.PositiveIntegerField()
    specialization = models.CharField(max_length=100)

    photo = models.ImageField(upload_to="chefs", blank=True, null=True)

    is_active = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)
    experience = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    contact_number = models.CharField(max_length=15)

    photo = models.ImageField(upload_to="staff", blank=True, null=True)

    is_active = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="gallery")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

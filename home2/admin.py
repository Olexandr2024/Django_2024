from django.contrib import admin
from .models import Category, Dish, Dish, Chef, Staff, Gallery, Contacts


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_visible", "sort", "sreated_at", "updated_at")
    list_editable = ("is_visible", "sort")
    list_filter = ("is_visible", "sreated_at", "updated_at")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    date_hierarchy = "sreated_at"


admin.site.register(Dish)


class DishAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "weight",
        "is_available",
        "created_at",
        "updated_at",
    )
    search_fields = ("name",)
    list_filter = ("is_available", "created_at")
    ordering = ("created_at",)


@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ("name", "specialization", "experience", "created_at")
    search_fields = ("name", "specialization")
    list_filter = ("experience", "created_at")
    ordering = ("created_at",)


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "contact_number", "created_at")
    search_fields = ("name", "position")
    list_filter = ("position", "created_at")
    ordering = ("created_at",)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "created_at")
    search_fields = ("title",)
    list_filter = ("created_at",)
    ordering = ("created_at",)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone_number", "created_at")
    search_fields = ("name", "email")
    list_filter = ("created_at",)
    ordering = ("created_at",)

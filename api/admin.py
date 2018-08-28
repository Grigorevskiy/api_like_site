from django.contrib import admin
from .models import News, NewsPhoto, Category, Journey, JourneyPhoto


class NewsPhotoInline(admin.TabularInline):
    model = NewsPhoto
    extra = 0


class JourneyPhotoInline(admin.TabularInline):
    model = JourneyPhoto
    extra = 0


class NewsAdmin(admin.ModelAdmin):
    """Add photos to Item in Admin"""
    inlines = [NewsPhotoInline]


class JouneyAdmin(admin.ModelAdmin):
    """Add photos to Item in Admin"""
    inlines = [JourneyPhotoInline]


admin.site.register(News, NewsAdmin)
admin.site.register(Category)
admin.site.register(Journey, JouneyAdmin)
from django.contrib import admin
from donationapp.models import Donation, Category, SubCategory, Request, RequestMatch, DonationMatch
# Register your models here.

class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    fieldsets = [(None, {'fields': ['title', 'order']}), ]
    inlines = [SubCategoryInline]

admin.site.register(Donation)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Request)
admin.site.register(RequestMatch)
admin.site.register(DonationMatch)

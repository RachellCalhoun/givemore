
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.


class Donation(models.Model):
    image = models.ImageField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=20)
    details = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)
    # contact_method = models.ForeignKey('ContactMethod', blank=True, null=True)
    NEW = 'New'
    LIKENEW = 'Like New'
    VERYGOOD = 'Very Good'
    GOOD = 'Good'
    ACCEPTABLE = 'Acceptable'
    CONDITION_CHOICES = (
        (NEW, 'New'),
        (LIKENEW, 'Like New'),
        (VERYGOOD, 'Very Good'),
        (GOOD, 'Good'),
        (ACCEPTABLE, 'Acceptable')
        )
    condition = models.CharField(
        max_length=15, choices=CONDITION_CHOICES, default=NEW)

    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(
        'SubCategory',
        on_delete=models.CASCADE, blank=True, null=True)

    def publish(self):
    	self.published_date = timezone.now()
    	self.save()

    def __str__(self):
    	return self.item

class Category(models.Model):
    order = models.PositiveIntegerField(help_text="Enter a number. 1 will be on the left.")
    title = models.CharField(null=True, max_length=100)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title



class SubCategory(models.Model):
	order = models.PositiveIntegerField(help_text="Enter a number.")
	title = models.CharField(null=True, max_length=100)
	link = models.CharField(blank=True, null=True, max_length=100)
	category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )

	def __str__(self):
		return self.title

class Request(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=20)
    details = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE, blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True,  default=timezone.now)
	# contact_method = models.ForeignKey('ContactMethod', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.item

class UserProfile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username

class ContactMethod(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    email = models.EmailField(max_length=70)
    phone_num = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_num], max_length=15, blank=True) # validators should be a list
    PHONE = "Phone Call"
    EMAIL = "Email"
    POSTCATEGORY = (
        (PHONE, 'Phone Call'),
        (EMAIL, 'Send Email'),
        )
    contact_method = models.CharField(max_length=5, choices=POSTCATEGORY, default=EMAIL)

    def __str__(self):
        return self.contact_method

class DonationMatch(models.Model):
    donation = models.ForeignKey('Donation', blank=True, null=True, related_name='donateobj', on_delete=models.CASCADE)
    interested = models.ForeignKey(User, on_delete=models.CASCADE)
    approve_contact = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "donation matches"

class RequestMatch(models.Model):
    request = models.ForeignKey('Request', blank=True, null=True, on_delete=models.CASCADE)
    interested = models.ForeignKey(User, on_delete=models.CASCADE)
    approve_contact = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "request matches"

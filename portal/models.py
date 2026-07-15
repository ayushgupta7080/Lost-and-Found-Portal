# portal/models.py
from django.db import models
from django.contrib.auth.models import User

# Extended user profile
class Profile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)  # required, always given at registration
    email = models.EmailField(blank=True, null=True)  # made optional to avoid migration errors
    contact = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.full_name


# Lost Item model
class LostItem(models.Model):
    CATEGORY_CHOICES = [
        ('Electronics', 'Electronics'),
        ('Wallet/Bag', 'Wallet/Bag'),
        ('Keys', 'Keys'),
        ('Jewelry', 'Jewelry'),
        ('Other', 'Other')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # optional, not everyone writes long descriptions
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='lost_items/', blank=True, null=True)
    date_lost = models.DateField(auto_now_add=True)
    is_claimed = models.BooleanField(default=False)
    claimed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='claimed_lost_items')
    returned = models.BooleanField(default=False)  # True if admin confirms returned

    def __str__(self):
        return f"{self.title} - {self.user.username}"


# Found Item model
class FoundItem(models.Model):
    CATEGORY_CHOICES = [
        ('Electronics', 'Electronics'),
        ('Wallet/Bag', 'Wallet/Bag'),
        ('Keys', 'Keys'),
        ('Jewelry', 'Jewelry'),
        ('Other', 'Other')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='found_items/', blank=True, null=True)
    date_found = models.DateField(auto_now_add=True)
    is_claimed = models.BooleanField(default=False)
    claimed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='claimed_found_items')
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.user.username}"


# History of returned items (optional, can be used for admin tracking)
class ItemHistory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='history_items/', blank=True, null=True)
    original_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_posted = models.DateField(blank=True, null=True)  # made optional to avoid migration issues
    date_returned = models.DateField(auto_now_add=True)
    item_type = models.CharField(max_length=10, choices=[('Lost', 'Lost'), ('Found', 'Found')], blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.original_user.username if self.original_user else 'Unknown'}"

from django.db import models
from django.utils.text import slugify

MYANMAR_DIVISIONS = [
    # States
    ('Chin', 'Chin'),
    ('Kachin', 'Kachin'),
    ('Kayah', 'Kayah'),
    ('Kayin', 'Kayin'),
    ('Mon', 'Mon'),
    ('Rakhine', 'Rakhine'),
    ('Shan', 'Shan'),
    # Regions
    ('Ayeyarwaddy', 'Ayeyarwaddy'),
    ('Bago', 'Bago'),
    ('Magway', 'Magway'),
    ('Mandalay', 'Mandalay'),
    ('Sagaing', 'Sagaing'),
    ('Tanintharyi', 'Tanintharyi'),
    ('Yangon', 'Yangon'),
    # Union Territory
    ('Nay Pyi Taw', 'Nay Pyi Taw'),
]

class CharityGuide(models.Model):
    myanmar_name   = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    address  = models.TextField()
    region = models.CharField(max_length=255, choices=MYANMAR_DIVISIONS, default="Yangon")
    is_published = models.BooleanField(default=False)
    map_link = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    fb_page = models.URLField(blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    detail = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
class CharityImage(models.Model):
    charity      = models.ForeignKey(
        CharityGuide, related_name="images", on_delete=models.CASCADE
    )
    image        = models.ImageField(upload_to="uya/charity_guides/")  
    caption      = models.CharField(max_length=255, blank=True)
    uploaded_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.charity.name}"

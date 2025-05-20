from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    CATEGORY_CHOICES = [
        ("UPCOMING", "Upcoming"),
        ("ONGOING",  "Ongoing"),
        ("PAST",     "Past"),
    ]

    title        = models.CharField(max_length=255)
    slug         = models.SlugField(max_length=255, unique=True, blank=True)
    description  = models.TextField()
    category     = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default="UPCOMING")
    start_date   = models.DateField()
    end_date     = models.DateField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class ProjectImage(models.Model):
    project      = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE
    )
    image        = models.ImageField(upload_to="uya/projects/")  # stored on Cloudinary
    caption      = models.CharField(max_length=255, blank=True)
    uploaded_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.project.title}"

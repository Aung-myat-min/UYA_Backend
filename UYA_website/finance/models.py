from django.db import models

class FinancialStatement(models.Model):
    statement_name = models.CharField(max_length=255)
    release_date = models.DateField()
    statement_link = models.URLField()
    is_published = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.statement_name} ({self.release_date})"
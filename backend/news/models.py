from django.db import models
class Author(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)


class News(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    summary = models.TextField()
    author = models.ManyToManyField(Author)
    # image =
    pub_date = models.DateTimeField(null=True, blank=True)  # Make it manually editable
    update_date = models.DateTimeField(auto_now=True)  # Set on every update
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title




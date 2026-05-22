from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('languages', 'Languages'),
        ('frameworks', 'Frameworks & Libraries'),
        ('cloud_db', 'Cloud & Databases'),
        ('tools', 'Tools & Platforms'),
        ('concepts', 'Concepts'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ProjectBullet(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bullets')
    text = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']


class Experience(models.Model):
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.role} at {self.company}"


class ExperienceBullet(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='bullets')
    text = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    gpa = models.CharField(max_length=20)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    coursework = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.degree


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

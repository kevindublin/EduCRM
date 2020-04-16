from django.db import models

class Student(models.Model):
    first_name = models.CharField("First Name", max_length=50)
    last_name = models.CharField("Last Name", max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)
    address_two = models.TextField(blank=True, null=True)
    city = models.CharField("City", max_length=50, null=True)
    state = models.CharField("State", max_length=30, null=True)
    zip_code = models.CharField(max_length=7, null=True)
    bio = models.TextField(blank=True, null=True)
    created = models.DateTimeField("Created at", auto_now_add=True)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'contact_info'
        managed = True
        verbose_name = 'student'
        verbose_name_plural = 'students'

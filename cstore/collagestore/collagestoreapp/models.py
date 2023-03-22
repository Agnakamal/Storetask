from django.db import models


# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    wiki_page = models.URLField()

    def __str__(self):
        return self.dept_name


class Courses(models.Model):
    course_name = models.CharField(max_length=50)
    course_dept = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name


class Materials(models.Model):
    item = models.CharField(max_length=50)

    def __str__(self):
        return self.item


class Order(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    GENDER_CHOICE = [('m', "Male"), ('f', "Female"), ('o', "Others")]
    gender = models.CharField(choices=GENDER_CHOICE, max_length=1)
    phone_number = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    PURPOSES = [('eq', "Enquiry"), ('po', "Place Order"), ('r', "Return")]
    purpose = models.CharField(max_length=2, choices=PURPOSES)
    materials = models.ManyToManyField(Materials)

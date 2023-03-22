from .models import Department


def departments_dropdown(requests):
    departments = Department.objects.all()
    return dict(departments=departments)
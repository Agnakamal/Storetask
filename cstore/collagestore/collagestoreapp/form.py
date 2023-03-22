
from .models import Order, Courses, Department
from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order


        fields = '__all__'
        widgets = {
            'department': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(format='%d/%m/%Y',attrs={'class': 'form-control','type': 'date'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'purpose': forms.Select(attrs={'class': 'form-control'}),
            'materials':forms.CheckboxSelectMultiple()

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Courses.objects.none()

        if 'department' in self.data:
            try:
                dept_id = int(self.data.get('department'))
                self.fields['course'].queryset = Courses.objects.filter(course_dept=dept_id).order_by('course_name')
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('course_name')

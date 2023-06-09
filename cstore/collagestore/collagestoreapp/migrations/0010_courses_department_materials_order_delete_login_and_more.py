# Generated by Django 4.1.3 on 2023-03-20 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collagestoreapp', '0009_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=100)),
                ('wiki_page', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Others')], max_length=1)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('purpose', models.CharField(choices=[('eq', 'Enquiry'), ('po', 'Place Order'), ('r', 'Return')], max_length=2)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collagestoreapp.courses')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collagestoreapp.department')),
                ('materials', models.ManyToManyField(to='collagestoreapp.materials')),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
        migrations.DeleteModel(
            name='register',
        ),
        migrations.AddField(
            model_name='courses',
            name='course_dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collagestoreapp.department'),
        ),
    ]

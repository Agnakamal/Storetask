# Generated by Django 4.1.3 on 2023-03-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collagestoreapp', '0004_rename_emailid_register_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=250),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.CharField(max_length=250),
        ),
    ]

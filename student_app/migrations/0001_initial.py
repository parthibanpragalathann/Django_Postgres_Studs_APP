# Generated by Django 3.2.7 on 2021-09-13 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=200)),
                ('RollNumber', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('DateofBirth', models.DateField(blank=True, help_text='Date of Birth')),
                ('marks', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
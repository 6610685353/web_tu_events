# Generated by Django 5.1.1 on 2024-11-12 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_tu_events', '0004_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
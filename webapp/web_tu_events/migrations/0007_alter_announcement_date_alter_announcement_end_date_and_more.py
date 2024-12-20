# Generated by Django 5.1.1 on 2024-11-12 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_tu_events', '0006_alter_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='end_date',
            field=models.DateTimeField(help_text='กรอกวันที่สิ้นสุดกิจกรรม'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='start_date',
            field=models.DateTimeField(help_text='กรอกวันที่เริ่มกิจกรรม'),
        ),
    ]

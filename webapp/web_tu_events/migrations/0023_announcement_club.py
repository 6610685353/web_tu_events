# Generated by Django 5.1.1 on 2024-11-30 04:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_tu_events', '0022_student_club'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web_tu_events.club'),
        ),
    ]

# Generated by Django 5.1.1 on 2024-11-30 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_tu_events', '0024_alter_announcement_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web_tu_events.student'),
        ),
    ]

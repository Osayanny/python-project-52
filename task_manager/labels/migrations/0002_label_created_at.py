# Generated by Django 5.1.5 on 2025-03-15 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2025-03-03 14:28:00'),
            preserve_default=False,
        ),
    ]

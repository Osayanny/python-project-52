# Generated by Django 5.1.5 on 2025-03-15 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0002_alter_task_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('tasks', models.ManyToManyField(to='tasks.task')),
            ],
        ),
    ]

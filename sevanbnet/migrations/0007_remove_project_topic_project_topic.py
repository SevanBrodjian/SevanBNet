# Generated by Django 4.0.6 on 2022-07-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sevanbnet', '0006_remove_project_topic_project_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='topic',
        ),
        migrations.AddField(
            model_name='project',
            name='topic',
            field=models.ManyToManyField(blank=True, to='sevanbnet.topic'),
        ),
    ]
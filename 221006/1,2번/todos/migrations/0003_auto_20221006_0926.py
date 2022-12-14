# Generated by Django 3.2.13 on 2022-10-06 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_rename_article_todo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='user',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='content',
        ),
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 3.1.7 on 2022-10-06 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eithers', '0003_comment_pick'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pick',
            field=models.BooleanField(),
        ),
    ]
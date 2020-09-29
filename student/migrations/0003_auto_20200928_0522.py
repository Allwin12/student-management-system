# Generated by Django 3.1.1 on 2020-09-28 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='section',
            field=models.CharField(default='A', max_length=10),
            preserve_default=False,
        ),
    ]
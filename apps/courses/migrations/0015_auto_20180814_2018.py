# Generated by Django 2.0.8 on 2018-08-14 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20180814_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='courses', to='courses.Tag', verbose_name='课程标签'),
        ),
    ]

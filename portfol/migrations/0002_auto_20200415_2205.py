# Generated by Django 3.0.5 on 2020-04-15 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='images/portfol'),
        ),
    ]

# Generated by Django 4.2 on 2023-05-01 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_cont_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(default='', upload_to='upload images'),
        ),
    ]

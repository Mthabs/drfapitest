# Generated by Django 3.2.23 on 2023-12-20 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_rgq6aq', upload_to='images/'),
        ),
    ]
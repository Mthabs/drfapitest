# Generated by Django 3.2.23 on 2023-12-20 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_yansvohttps://res.cloudinary.com/dnt7oro5y/image/upload/v1702078965/default_profile_yansvo.jpg', upload_to='images/'),
        ),
    ]
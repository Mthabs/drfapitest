# Generated by Django 3.2.23 on 2023-12-20 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='https://res.cloudinary.com/dnt7oro5y/image/upload/v1702078965/default_post_wv7bvz.jpg', upload_to='images/'),
        ),
    ]

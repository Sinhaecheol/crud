# Generated by Django 2.2.1 on 2019-06-02 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]

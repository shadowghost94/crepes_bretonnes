# Generated by Django 5.0 on 2024-02-14 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_categorie_article_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
    ]

# Generated by Django 4.1.5 on 2023-02-21 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_rename_scopes_article_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tag',
            new_name='scopes',
        ),
    ]

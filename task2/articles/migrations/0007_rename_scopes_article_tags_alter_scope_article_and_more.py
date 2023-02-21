# Generated by Django 4.1.5 on 2023-02-21 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_article_scopes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='scopes',
            new_name='tags',
        ),
        migrations.AlterField(
            model_name='scope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag'),
        ),
    ]

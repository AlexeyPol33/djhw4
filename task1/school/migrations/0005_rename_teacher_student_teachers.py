# Generated by Django 4.1.5 on 2023-02-20 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_alter_student_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher',
            new_name='teachers',
        ),
    ]

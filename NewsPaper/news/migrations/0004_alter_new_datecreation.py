# Generated by Django 4.0.3 on 2022-03-28 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_new_datecreation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='dateCreation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата публикации'),
        ),
    ]

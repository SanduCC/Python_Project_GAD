# Generated by Django 3.2.9 on 2021-12-12 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_produse_produs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produs',
            old_name='categorie',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='produs',
            old_name='descriere',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='produs',
            old_name='denumire',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='produs',
            old_name='pret',
            new_name='price',
        ),
    ]
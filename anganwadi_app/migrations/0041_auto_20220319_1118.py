# Generated by Django 3.2.12 on 2022-03-19 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anganwadi_app', '0040_tbl_childfoodstock_tbl_childfoodstockrequest_tbl_totalchildfoodstock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_totalchildfoodstock',
            old_name='pfood_id',
            new_name='food_id',
        ),
        migrations.RenameField(
            model_name='tbl_totalchildfoodstock',
            old_name='pfood_totalStock',
            new_name='food_totalStock',
        ),
    ]

# Generated by Django 3.2.12 on 2022-03-08 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anganwadi_app', '0007_tbl_pwomenfood_tbl_userfood'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_userfood',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

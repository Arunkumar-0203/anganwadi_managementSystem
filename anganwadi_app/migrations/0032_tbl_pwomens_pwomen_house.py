# Generated by Django 3.2.12 on 2022-03-11 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anganwadi_app', '0031_alter_tbl_complaint_complainttype_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_pwomens',
            name='pwomen_house',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
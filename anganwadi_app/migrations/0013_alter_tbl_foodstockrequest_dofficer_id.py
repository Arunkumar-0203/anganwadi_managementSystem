# Generated by Django 3.2.12 on 2022-03-09 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anganwadi_app', '0012_rename_a_id_tbl_foodstockrequest_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_foodstockrequest',
            name='dofficer_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='anganwadi_app.districtofficer'),
        ),
    ]

# Generated by Django 3.2.12 on 2022-03-10 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anganwadi_app', '0017_auto_20220310_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_pfoodstock',
            name='pfood_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anganwadi_app.tbl_pwomenfood'),
        ),
        migrations.AlterField(
            model_name='tbl_totalpfoodstock',
            name='pfood_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anganwadi_app.tbl_pwomenfood'),
        ),
    ]

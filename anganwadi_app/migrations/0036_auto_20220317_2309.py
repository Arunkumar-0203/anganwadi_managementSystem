# Generated by Django 3.2.12 on 2022-03-17 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anganwadi_app', '0035_alter_tbl_pfoodbooking_pwomenfoodservice_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_foodbooking',
            name='anganwadi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='anganwadi_app.anganawadi'),
        ),
        migrations.AddField(
            model_name='tbl_pfoodbooking',
            name='anganwadi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='anganwadi_app.anganawadi'),
        ),
    ]
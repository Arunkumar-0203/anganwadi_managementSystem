# Generated by Django 3.2.12 on 2022-03-10 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anganwadi_app', '0019_tbl_pfoodstockrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_name', models.CharField(max_length=100, null=True)),
                ('child_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='tbl_foodstock',
            name='food_stock',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tbl_foodstockrequest',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tbl_pfoodstock',
            name='pfood_stock',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tbl_pfoodstockrequest',
            name='pquantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tbl_totalfoodstock',
            name='food_totalStock',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='tbl_child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_name', models.CharField(max_length=100, null=True)),
                ('child_age', models.CharField(max_length=100, null=True)),
                ('child_image', models.ImageField(null=True, upload_to='', verbose_name='images/')),
                ('child_fathername', models.CharField(max_length=100, null=True)),
                ('child_mothername', models.CharField(max_length=100, null=True)),
                ('child_gender', models.CharField(max_length=100, null=True)),
                ('child_status', models.CharField(max_length=100, null=True)),
                ('birthcertificate', models.DateField(max_length=100, null=True)),
                ('child_hname', models.CharField(max_length=100, null=True)),
                ('child_street', models.CharField(max_length=100, null=True)),
                ('child_pin', models.CharField(max_length=100, null=True)),
                ('child_contact', models.CharField(max_length=100, null=True)),
                ('a_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('child_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anganwadi_app.child')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anganwadi_app.location')),
                ('place_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anganwadi_app.place')),
            ],
        ),
    ]

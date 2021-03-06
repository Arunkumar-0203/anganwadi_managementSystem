# Generated by Django 3.2.12 on 2022-03-19 04:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anganwadi_app', '0039_auto_20220318_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_totalchildfoodstock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pfood_totalStock', models.IntegerField(max_length=100, null=True)),
                ('pfood_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anganwadi_app.tbl_pwomenfood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_childfoodstockrequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fsrequest_date', models.DateField(auto_now_add=True)),
                ('quantity', models.IntegerField(null=True)),
                ('f_status', models.CharField(max_length=100, null=True)),
                ('dofficer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='anganwadi_app.districtofficer')),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anganwadi_app.tbl_child')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anganwadi_app.anganawadi')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_childfoodstock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_stock', models.IntegerField(null=True)),
                ('foodstock_date', models.DateField(max_length=100, null=True)),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anganwadi_app.tbl_pwomenfood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

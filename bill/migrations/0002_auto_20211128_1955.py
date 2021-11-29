# Generated by Django 3.2.3 on 2021-11-28 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='bill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bill.bill'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='Gtotal',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='byerGSTN',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='invoice_no',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='to',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='total',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='particulars',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='qty',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='rate',
            field=models.FloatField(null=True),
        ),
    ]

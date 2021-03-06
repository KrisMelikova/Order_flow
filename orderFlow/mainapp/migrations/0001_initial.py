# Generated by Django 3.2.4 on 2021-06-11 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('NEW', 'new'), ('ACCEPTED', 'accepted'), ('FAILED', 'failed')], default='NEW', max_length=12, verbose_name='order status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='order created date in UTC')),
                ('external_id', models.CharField(max_length=128, verbose_name='identifier of the order in external system')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='product name')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='how many items are included in order detail')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='products price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.order', verbose_name='reference to order entity')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product', verbose_name='reference to product entity')),
            ],
        ),
    ]

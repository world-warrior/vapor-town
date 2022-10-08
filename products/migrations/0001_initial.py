# Generated by Django 3.2.14 on 2022-10-08 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programmatic_name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=254)),
                ('brand', models.CharField(blank=True, max_length=254, null=True)),
                ('description', models.TextField()),
                ('current_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('accumulative_rating', models.IntegerField(blank=True, default=0, null=True)),
                ('Number_of_ratings', models.IntegerField(blank=True, default=0, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('stock_level', models.IntegerField()),
                ('in_stock', models.BooleanField(default=True)),
                ('has_sale', models.BooleanField(default=False)),
                ('rrp', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discounted_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_products.product_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='DisposableVapes',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product')),
                ('battery_size', models.CharField(blank=True, max_length=254, null=True)),
                ('max_puffs', models.CharField(blank=True, max_length=254, null=True)),
                ('flavour', models.CharField(blank=True, max_length=254, null=True)),
                ('nicotine_strength', models.CharField(choices=[('0', '0mg'), ('10', '10mg'), ('20', '20mg')], default='0', max_length=2)),
                ('liquid_capacity', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Disposable Vapes',
            },
            bases=('products.product',),
        ),
    ]

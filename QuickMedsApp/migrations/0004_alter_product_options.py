# Generated by Django 5.1.6 on 2025-03-03 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuickMedsApp', '0003_alter_product_expiry_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]

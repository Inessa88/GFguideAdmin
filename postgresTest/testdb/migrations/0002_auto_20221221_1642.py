# Generated by Django 3.2.16 on 2022-12-21 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='productpictures',
            options={'verbose_name': 'Picture', 'verbose_name_plural': 'Pictures'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='restaurants',
            options={'verbose_name': 'Restaurant', 'verbose_name_plural': 'Restaurants'},
        ),
        migrations.AlterModelOptions(
            name='siteusers',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.RenameField(
            model_name='products',
            old_name='post_data',
            new_name='post_date',
        ),
        migrations.RemoveField(
            model_name='products',
            name='ingredient_picture',
        ),
        migrations.RemoveField(
            model_name='restaurants',
            name='user',
        ),
        migrations.AlterField(
            model_name='products',
            name='main_picture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_main_picture', to='testdb.productpictures'),
        ),
        migrations.AlterField(
            model_name='products',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testdb.siteusers'),
        ),
    ]


import Shop.models
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_icecream_person_icecreamstand_child'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='товар')),
                ('content', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='цена')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='опубликовано')),
                ('count', models.IntegerField(default=0, validators=[Shop.models.validate_even_number], verbose_name='количество')),
            ],
            options={
                'verbose_name': 'объявление',
                'verbose_name_plural': 'объявления',
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='название')),
            ],
            options={
                'verbose_name': 'рубрика',
                'verbose_name_plural': 'рубрики',
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='child',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='icecreamstand',
            name='items',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='bb',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Shop.rubric', verbose_name='рубрика'),
        ),
        migrations.DeleteModel(
            name='Child',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='IceCream',
        ),
        migrations.DeleteModel(
            name='IceCreamStand',
        ),
    ]

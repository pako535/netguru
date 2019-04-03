# Generated by Django 2.2 on 2019-04-03 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.CharField(default='None', max_length=100, verbose_name='Actros'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='awards',
            field=models.CharField(default='None', max_length=200, verbose_name='Awards'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='box_office',
            field=models.CharField(default='None', max_length=15, verbose_name='BoxOffice'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.CharField(default='None', max_length=50, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(default='None', max_length=50, verbose_name='Director'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='dvd',
            field=models.CharField(default='None', max_length=15, verbose_name='DVD'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(default='None', max_length=100, verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdbID',
            field=models.CharField(default='None', max_length=30, verbose_name='imdbID'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(default='None', max_length=50, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_type',
            field=models.CharField(default='None', max_length=10, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='plot',
            field=models.CharField(default='None', max_length=300, verbose_name='Plot'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='production',
            field=models.CharField(default='None', max_length=100, verbose_name='Production'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rank',
            field=models.IntegerField(default=0, verbose_name='Rank'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rated',
            field=models.CharField(default='None', max_length=10, verbose_name='Rated'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='ratings',
            field=models.CharField(default='None', max_length=300, verbose_name='Ratings'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='released',
            field=models.CharField(default='None', max_length=15, verbose_name='Released'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='runtime',
            field=models.CharField(default='None', max_length=15, verbose_name='Runtime'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='writer',
            field=models.CharField(default='None', max_length=600, verbose_name='Writer'),
        ),
    ]
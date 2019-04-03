# Generated by Django 2.2 on 2019-04-03 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000, verbose_name='Content of comment')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('year_of_release', models.IntegerField(verbose_name='Year')),
                ('rated', models.CharField(max_length=10, verbose_name='Rated')),
                ('released', models.CharField(max_length=15, verbose_name='Released')),
                ('runtime', models.CharField(max_length=15, verbose_name='Runtime')),
                ('genre', models.CharField(max_length=100, verbose_name='Genre')),
                ('director', models.CharField(max_length=50, verbose_name='Director')),
                ('writer', models.CharField(max_length=600, verbose_name='Writer')),
                ('actors', models.CharField(max_length=100, verbose_name='Actros')),
                ('plot', models.CharField(max_length=300, verbose_name='Plot')),
                ('language', models.CharField(max_length=50, verbose_name='Language')),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
                ('awards', models.CharField(max_length=200, verbose_name='Awards')),
                ('poster', models.URLField(verbose_name='Poster')),
                ('ratings', models.CharField(max_length=300, verbose_name='Ratings')),
                ('metascore', models.IntegerField(verbose_name='Metascore')),
                ('imdbRating', models.FloatField(verbose_name='imdbRating')),
                ('imdbVotes', models.FloatField(verbose_name='imdbVotes')),
                ('imdbID', models.CharField(max_length=30, verbose_name='imdbID')),
                ('movie_type', models.CharField(max_length=10, verbose_name='Type')),
                ('dvd', models.CharField(max_length=15, verbose_name='DVD')),
                ('box_office', models.CharField(max_length=15, verbose_name='BoxOffice')),
                ('production', models.CharField(max_length=100, verbose_name='Production')),
                ('website', models.URLField(verbose_name='Website')),
                ('rank', models.IntegerField(verbose_name='Rank')),
            ],
        ),
        migrations.CreateModel(
            name='AssociateTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Comments', verbose_name='Commnets')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Movie', verbose_name='Movie')),
            ],
        ),
    ]

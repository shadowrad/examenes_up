# Generated by Django 2.1.7 on 2019-02-19 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0005_pregunta_posibilidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=100, verbose_name='Tag')),
            ],
            options={
                'ordering': ['Descripcion'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together={('Descripcion',)},
        ),
        migrations.AddField(
            model_name='pregunta',
            name='tags',
            field=models.ManyToManyField(to='preguntas.Tag'),
        ),
    ]
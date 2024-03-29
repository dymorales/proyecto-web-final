# Generated by Django 4.2.1 on 2023-06-28 02:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombre', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('password', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=40, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CategoriaNoticia',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id_TipoUsuario', models.AutoField(db_column='id_TipoUsuario', primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id_Noticia', models.AutoField(db_column='id_Noticia', primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=500)),
                ('detalle', models.CharField(max_length=4000)),
                ('contenido', models.CharField(blank=True, max_length=10000)),
                ('fecha', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('ubicacion', models.CharField(max_length=40)),
                ('img', models.CharField(default='', max_length=150)),
                ('aprobada', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(db_column='Nombre', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_Categoria', models.ForeignKey(db_column='Descripcion', default='', on_delete=django.db.models.deletion.CASCADE, to='appWeb.categorianoticia')),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='id_TipoUsuario',
            field=models.ForeignKey(db_column='id_TipoUsuario', default=2, on_delete=django.db.models.deletion.CASCADE, to='appWeb.tipousuario'),
        ),
    ]

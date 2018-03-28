# Generated by Django 2.0.3 on 2018-03-28 08:39

from django.db import migrations, models
import django.db.models.deletion
import webconfig.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, validators=[webconfig.models.validate_hostname])),
            ],
        ),
        migrations.CreateModel(
            name='FQDN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, validators=[webconfig.models.validate_hostname])),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webconfig.Domain')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=128)),
                ('auth_level', models.SmallIntegerField(choices=[(1, 'SSO'), (3, 'SSO + Basic Auth'), (5, 'Public + SSO')], default=1)),
                ('allow_cors', models.BooleanField(default=False)),
                ('allow_websockets', models.BooleanField(default=False)),
                ('rules', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=False)),
                ('allow_https', models.BooleanField(default=True)),
                ('allow_http', models.BooleanField(default=False)),
                ('rules', models.TextField()),
                ('status', models.SmallIntegerField(choices=[(1, 'Production'), (2, 'UAT'), (3, 'Development'), (4, 'Redirect')], default=1)),
                ('availability', models.SmallIntegerField(choices=[(1, 'Internal'), (2, 'Public')], default=1)),
                ('aliases', models.ManyToManyField(related_name='alias_for', to='webconfig.FQDN')),
                ('fqdn', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webconfig.FQDN')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webconfig.Site'),
        ),
        migrations.AlterUniqueTogether(
            name='site',
            unique_together={('fqdn',)},
        ),
        migrations.AlterUniqueTogether(
            name='fqdn',
            unique_together={('name', 'domain')},
        ),
    ]

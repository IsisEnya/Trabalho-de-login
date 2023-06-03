

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='ultimo login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designa que este usuário tem todas as permissões sem atribuí-las explicitamente', verbose_name='superuser status')),
                ('nome', models.CharField(error_messages={'unique': 'usuario com o mesmo nome ja existe.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('primeiro_nome', models.CharField(blank=True, max_length=30, verbose_name='primeio nome')),
                ('ultimo_nome', models.CharField(blank=True, max_length=150, verbose_name='ultimo nome')),
                ('cep', models.CharField(blank=True, max_length=9, verbose_name='CEP')),
                ('location', models.CharField(blank=True, max_length=50, verbose_name='Localidade')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email ')),
                ('senha', models.CharField(max_length=50, verbose_name='Senha')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='especificacoes do usuario.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

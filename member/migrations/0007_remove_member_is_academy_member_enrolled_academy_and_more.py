# Generated by Django 5.1.3 on 2024-12-28 03:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0011_student'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('member', '0006_student_enrolled_academy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='is_academy',
        ),
        migrations.AddField(
            model_name='member',
            name='enrolled_academy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='academy.academy'),
        ),
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_type',
            field=models.CharField(choices=[('student', '수강생'), ('academy_admin', '학원운영자')], default='student', max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

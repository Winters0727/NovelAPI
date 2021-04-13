# Generated by Django 3.2 on 2021-04-12 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='like_books',
            field=models.ManyToManyField(blank=True, related_name='like_users', to='book.Book'),
        ),
        migrations.AddField(
            model_name='author',
            name='like_reviews',
            field=models.ManyToManyField(blank=True, related_name='like_users', to='book.Review'),
        ),
        migrations.AddField(
            model_name='author',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
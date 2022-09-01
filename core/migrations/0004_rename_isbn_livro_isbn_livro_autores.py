# Generated by Django 4.1 on 2022-08-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_autor_options_livro"),
    ]

    operations = [
        migrations.RenameField(
            model_name="livro",
            old_name="ISBN",
            new_name="isbn",
        ),
        migrations.AddField(
            model_name="livro",
            name="autores",
            field=models.ManyToManyField(related_name="livros", to="core.autor"),
        ),
    ]

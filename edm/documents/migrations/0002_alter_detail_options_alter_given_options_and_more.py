# Generated by Django 5.0 on 2023-12-14 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="detail",
            options={
                "ordering": ["name"],
                "verbose_name": "Подробно",
                "verbose_name_plural": "Подробности",
            },
        ),
        migrations.AlterModelOptions(
            name="given",
            options={
                "ordering": ["name"],
                "verbose_name": "Тип передачи",
                "verbose_name_plural": "Типы передачи",
            },
        ),
        migrations.AlterModelOptions(
            name="implementers",
            options={
                "ordering": ["name"],
                "verbose_name": "Исполнитель",
                "verbose_name_plural": "Исполнители",
            },
        ),
        migrations.AlterModelOptions(
            name="numeration",
            options={
                "ordering": ["id"],
                "verbose_name": "Нумерация",
                "verbose_name_plural": "Нумерация",
            },
        ),
        migrations.AlterModelOptions(
            name="organization",
            options={
                "ordering": ["name"],
                "verbose_name": "Организация",
                "verbose_name_plural": "Организации",
            },
        ),
        migrations.AlterModelOptions(
            name="theme",
            options={
                "ordering": ["name"],
                "verbose_name": "Тема",
                "verbose_name_plural": "Темы",
            },
        ),
        migrations.RemoveField(
            model_name="document",
            name="from_where",
        ),
        migrations.AddField(
            model_name="document",
            name="from_doc",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="org_from",
                to="documents.organization",
                verbose_name="Откуда",
            ),
        ),
        migrations.AddField(
            model_name="document",
            name="where_doc",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="org_where",
                to="documents.organization",
                verbose_name="Куда",
            ),
        ),
        migrations.AlterField(
            model_name="document",
            name="area",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Участок"
            ),
        ),
        migrations.AlterField(
            model_name="document",
            name="detail",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="detail_doc",
                to="documents.detail",
                verbose_name="Детали",
            ),
        ),
        migrations.AlterField(
            model_name="document",
            name="file",
            field=models.FileField(
                blank=True, null=True, upload_to="docs/%Y/%m/%d/", verbose_name="Файл"
            ),
        ),
        migrations.AlterField(
            model_name="document",
            name="given",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="given_doc",
                to="documents.given",
                verbose_name="Передано",
            ),
        ),
        migrations.AlterField(
            model_name="document",
            name="implementers",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="implementers_doc",
                to="documents.implementers",
                verbose_name="Исполнитель",
            ),
        ),
        migrations.AlterField(
            model_name="document",
            name="size",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Размер файла"
            ),
        ),
        migrations.AlterField(
            model_name="document",
            name="theme",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="theme_doc",
                to="documents.theme",
                verbose_name="Тема",
            ),
        ),
        migrations.AlterField(
            model_name="document",
            name="who",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Кто"
            ),
        ),
    ]

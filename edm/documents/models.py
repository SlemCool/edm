from django.contrib.auth import get_user_model
from django.db import models

# from users.models import User

User = get_user_model()


class Organization(models.Model):
    """Модель для списка организаций"""

    name = models.CharField(
        verbose_name="Название организации",
        max_length=100,
        blank=False,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["-name"]
        verbose_name = "Организация"
        verbose_name_plural = "Организации"


class Numeration(models.Model):
    """Модель для счетчиков"""

    name = models.CharField(verbose_name="Наименование счетчика", max_length=50)
    num = models.PositiveIntegerField(
        verbose_name="Текущий номер", blank=False, null=False
    )

    def __str__(self) -> str:
        return self.name + " - " + str(self.num)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Нумерация"
        verbose_name_plural = "Нумерация"


class Theme(models.Model):
    """Модель для списка тем документа"""

    name = models.CharField(
        verbose_name="Тема документа", max_length=100, blank=False, null=False
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["-name"]
        verbose_name = "Тема"
        verbose_name_plural = "Темы"


class Detail(models.Model):
    """Модель для подробностей документа"""

    name = models.CharField(
        verbose_name="Подробно для документа", max_length=100, blank=False, null=False
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["-name"]
        verbose_name = "Подробно"
        verbose_name_plural = "Подробности"


class Given(models.Model):
    """Модель для типа передачи документа"""

    name = models.CharField(
        verbose_name="Тип передачи документа", max_length=100, blank=False, null=False
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["-name"]
        verbose_name = "Тип передачи"
        verbose_name_plural = "Типы передачи"


class Implementers(models.Model):
    """Модель для исполнителей документа"""

    name = models.CharField(
        verbose_name="Исполнитель", max_length=50, blank=False, null=False
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["-name"]
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"


class Document(models.Model):
    """Модель для создания документа"""

    INPUT_DOC = "ВХ"
    OUTPUT_DOC = "ИС"
    IN_OUT_DOC = "ВХ-ИС"
    DOCUMENT_TYPE_CHOICES = [
        (INPUT_DOC, "входящий"),
        (OUTPUT_DOC, "исходящий"),
        (IN_OUT_DOC, "входящий-исходящий"),
    ]
    doc_type = models.CharField(
        verbose_name="Тип документа",
        help_text="Укажите тип документа",
        max_length=5,
        choices=DOCUMENT_TYPE_CHOICES,
        blank=False,
    )
    from_where = models.ForeignKey(
        Organization,
        related_name="org_from",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name="Откуда-Куда",
    )
    area = models.CharField(
        verbose_name="Участок", max_length=100, blank=True, null=True
    )
    who = models.CharField(verbose_name="Кто", max_length=100, blank=True, null=True)

    input_num = models.PositiveIntegerField(
        verbose_name="Входящий номер", blank=True, null=True
    )
    output_num = models.PositiveIntegerField(
        verbose_name="Исходящий номер", blank=True, null=True
    )
    theme = models.ForeignKey(
        Theme,
        related_name="theme_doc",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name="Тема",
    )
    detail = models.ForeignKey(
        Detail,
        related_name="detail_doc",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name="Детали",
    )
    given = models.ForeignKey(
        Given,
        related_name="given_doc",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name="Передано",
    )
    file = models.FileField(
        verbose_name="Файл", upload_to="docs/%Y/%m/%d/", blank=True, null=True
    )
    size = models.PositiveIntegerField(
        verbose_name="Размер файла", blank=True, null=True
    )
    description = models.TextField(
        verbose_name="Прочее",
        help_text="Укажите прочие подробности",
        blank=True,
        null=True,
    )
    implementers = models.ForeignKey(
        Implementers,
        related_name="implementers_doc",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name="Исполнитель",
    )
    date_input_doc = models.DateTimeField(
        verbose_name="Дата входящего",
        help_text="Укажите дату входящего документа",
        blank=True,
        null=True,
    )
    date_output_doc = models.DateTimeField(
        verbose_name="Дата исходящего",
        help_text="Укажите дату исходящего документа",
        blank=True,
        null=True,
    )

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="author_doc",
        verbose_name="Автор создания",
    )
    modified_date = models.DateTimeField(
        "Дата изменения",
        auto_now=True,
    )
    created_date = models.DateTimeField(
        "Дата публикации",
        auto_now_add=True,
    )

    def __str__(self) -> str:
        theme = self.theme if self.theme else "Без темы"
        return (
            self.doc_type + " - " + theme + " - " + str(self.author)
        )

    class Meta:
        ordering = ["-id"]
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

from django.db import models
from users.models import User


class Document(models.Model):
    """Модель для создания документа"""

    reg = models.ForeignKey(
        Reg, related_name="doc_reg", on_delete=models.CASCADE, blank=True, null=True
    )
    title = models.CharField(max_length=100, blank=True, null=True)
    file = models.FileField(upload_to="./docs/", storage=fs, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    common = models.BooleanField(default=False)
    signature = models.CharField(max_length=500, blank=True, null=True)
    signature_end = models.BooleanField(default=False)
    hash = models.ForeignKey(
        Block, related_name="doc_h", on_delete=models.CASCADE, blank=True, null=True
    )
    cancel_description = models.CharField(max_length=500, blank=True, null=True)
    cancel_file = models.FileField(
        upload_to="./cancel_docs/", storage=fs, blank=True, null=True
    )
    file_cabinet = models.ForeignKey(
        FileCabinet,
        related_name="doc_fc",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    post_delete.connect(receiver=delete_doc)

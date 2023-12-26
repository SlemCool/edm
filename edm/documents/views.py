from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DocumentForm
from .models import Document
from .utils import paginator


def index(request) -> HttpResponse:
    template = "documents/index.html"
    documents = Document.objects.select_related("from_doc", "where_doc").all()
    context = {
        "page_obj": paginator(documents, request),
    }
    return render(request, template, context)


def document_incoming(request):
    template = "documents/index.html"
    documents = Document.objects.select_related("from_doc", "where_doc").filter(
        doc_type="ВХ"
    )
    context = {
        "page_obj": paginator(documents, request),
    }
    return render(request, template, context)


def document_outgoing(request):
    template = "documents/index.html"
    documents = Document.objects.select_related("from_doc", "where_doc").filter(
        doc_type="ИС"
    )
    context = {
        "page_obj": paginator(documents, request),
    }
    return render(request, template, context)


@login_required
def document_create(request):
    template = "documents/create_document.html"
    form = DocumentForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.author = request.user
        form.save()
        return redirect("documents:index")
    return render(request, template, {"form": form})


@login_required
def document_edit(request, document_id):
    template = "documents/create_document.html"
    document = get_object_or_404(Document, pk=document_id)
    if request.user != document.author:
        return redirect("documents:document_detail", document_id=document_id)
    form = DocumentForm(
        request.POST or None, files=request.FILES or None, instance=document
    )
    if form.is_valid():
        # form = form.save(commit=False)
        # form.author = request.user
        form.save()
        return redirect("documents:document_detail", document_id=document_id)
    context = {
        "document": document,
        "form": form,
        "is_edit": True,
    }
    return render(request, template, context)


def document_detail(request, document_id):
    template = "documents/document_detail.html"
    document = get_object_or_404(Document, pk=document_id)
    # comments = post.comments.all()
    # form = CommentForm(request.POST or None)
    # if form.is_valid():
    #     comment = form.save(commit=False)
    #     comment.author = request.user
    #     comment.post = post
    #     comment.save()
    #     return redirect('posts:post_detail', post_id=post_id)
    context = {
        "document": document,
        # 'form': form,
        # 'comments': comments,
    }
    return render(request, template, context)


from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
from .pdf_utils import extract_pdf_text, create_chunks
from .ollama_utils import ask_pdf

def upload_pdf(request):

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('upload_pdf')

    else:
        form = DocumentForm()

    return render(request, 'upload.html', {'form': form})


def chat_pdf(request):

    answer = ""

    if request.method == "POST":

        question = request.POST.get("question")

        doc = Document.objects.last()

        text = extract_pdf_text(doc.pdf.path)

        chunks = create_chunks(text)

        answer = ask_pdf(
            chunks,
            question
        )

    return render(
        request,
        "chat.html",
        {
            "answer": answer
        }
    )

from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def extract_pdf_text(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        text += (page.extract_text() or "") + "\n"

    return text
def create_chunks(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    return chunks



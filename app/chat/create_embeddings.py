from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.chat.vector_store.pinecone import vector_store


def create_embeddings_for_pdf(pdf_id: str, pdf_path: str):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    loader = PyPDFLoader(file_path=pdf_path)
    texts = loader.load_and_split(text_splitter=text_splitter)

    for text in texts:
        text.metadata = {
            "pdf-id": pdf_id,
            "page": text.metadata["page"],
            "text": text.page_content,
        }
    vector_store.add_documents(texts)

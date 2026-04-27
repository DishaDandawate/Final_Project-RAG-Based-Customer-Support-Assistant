from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

print("Starting RAG System...")

# Load PDF
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

print("System Ready ✅")

# Chat loop
while True:
    query = input("\nAsk a question (type 'exit' to quit): ").lower()

    if query == "exit":
        print("Exiting...")
        break

    found = False

   for doc in docs:
    if query in doc.page_content.lower():
        print("\nAnswer from document:\n")

        answer = doc.page_content.strip()

        # Show only first 2-3 lines (clean output)
        lines = answer.split("\n")
        for line in lines[:3]:
            print(line)

        found = True
        break

    if not found:
        print("\nEscalating to human support (HITL) ❗")
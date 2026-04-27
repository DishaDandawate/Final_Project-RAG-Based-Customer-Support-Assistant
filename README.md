# Final_Project-RAG-Based-Customer-Support-Assistant
# 📊 RAG-Based Customer Support Assistant

## 📌 Project Overview
This project implements a **Retrieval-Augmented Generation (RAG) based Customer Support Assistant**.  
The system uses a PDF knowledge base to answer user queries and provides relevant responses based on document content.

---

## 🎯 Objective
- To build a system that retrieves information from a PDF
- To answer user queries contextually
- To simulate Human-in-the-Loop (HITL) escalation for unmatched queries

---

## ⚙️ Features
- 📄 Load and process PDF document
- ✂️ Split text into smaller chunks
- 🔍 Retrieve relevant information based on user query
- 💬 Interactive command-line chatbot
- 👤 HITL escalation for unknown queries

---

## 🏗️ System Architecture
User → Input Query → Document Processing → Retrieval → Response / HITL

---

## 🧠 How It Works

1. PDF document is loaded
2. Text is extracted and split into chunks
3. User enters a query
4. System searches for matching content in chunks
5. If match found → display answer  
6. If no match → escalate to human support (HITL)

---

## 🛠️ Tech Stack

- Python
- LangChain
- PyPDF
- Text Splitter

---

## 📂 Project Structure
RAG_Project/ │ 
├── rag_app.py 
├── sample.pdf
├── requirements.txt 
├── HLD.pdf 
├── LLD.pdf 
├── Technical_Documentation.pdf 
├── README.md

---

## ▶️ How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run the project:
python rag_app.py

3. Ask questions in terminal:
What is refund policy?

---

## 🧪 Sample Queries

- What is refund policy?
- How to contact support?
- What are payment methods?

---

## 👤 HITL (Human-in-the-Loop)

If the system cannot find relevant information, it escalates the query to human support.

---

## ⚠️ Limitations

- Uses keyword-based matching (no advanced embeddings)
- Limited semantic understanding
- CLI-based interface only

---

## 🚀 Future Enhancements

- Integration with vector database (ChromaDB)
- Use of embeddings for better accuracy
- Web-based UI chatbot
- Multi-document support

---

## 📌 Conclusion

This project demonstrates the core concept of **RAG systems** by combining document retrieval and query-based response generation, along with HITL for better reliability.

---

## 🙌 Author

- Disha Dandawate

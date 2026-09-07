# 🤖 AI Article Generator

A simple **Django-based AI Article Generator** that uses Generative AI,
web research, RAG, and a chatbot to create informative articles.

---

## ✨ Features

- 📝 Generate articles from any topic
- 🌐 Research topics using Tavily
- 🤖 Generate articles using Google Gemini
- 🔎 Retrieval-Augmented Generation (RAG)
- 💬 Chat with generated articles
- 🧠 Conversation memory
- 🔗 View research sources
- 💾 Save articles
- ✏️ Edit saved articles
- 🗑️ Delete saved articles
- 👤 User authentication
- 📚 Personal article collection

---

## 🏗️ Built With

| Technology | Purpose |
|---|---|
| 🐍 Django | Web application & backend |
| 🤖 Google Gemini | Article generation & chatbot |
| 🔎 Tavily | Web research |
| 🦜 LangChain | AI/RAG pipeline |
| 🧠 Gemini Embeddings | Text embeddings |
| 🗄️ ChromaDB | Vector database |
| 🗃️ SQLite | Application database |
| 🎨 HTML & CSS | Frontend |

---

## 🐍 Django Backend

The application is built with Django.

Django handles:

- 👤 User registration & login
- 📝 Article management
- 💾 Saving articles
- ✏️ Updating articles
- 🗑️ Deleting articles
- 🔐 User-specific articles
- 🌐 URL routing
- 🎨 HTML templates

---

## 🤖 Generative AI

The application uses **Google Gemini** to generate articles
and answer questions about them.

The user provides a topic:

```text
Artificial Intelligence in Healthcare
```
The application researches the topic and generates
a structured article using the collected information.

🌐 Web Research

Tavily is used to search the web for relevant information.

User Topic
    ↓
Tavily Web Search
    ↓
Research Documents

This gives the AI external research to work with.

🔎 RAG Pipeline

The project uses Retrieval-Augmented Generation (RAG).

Research
   ↓
Document Splitting
   ↓
Embeddings
   ↓
ChromaDB
   ↓
Similarity Search
   ↓
Relevant Context
   ↓
Google Gemini
   ↓
Generated Article

This helps Gemini generate answers using relevant research
instead of relying only on its internal knowledge.

💬 AI Article Chat

After generating an article, users can ask questions about it.

Example:

User: What are the main benefits mentioned in the article?

AI: The main benefits include...

The chatbot uses:

🔎 Article retrieval
🧠 Conversation history
🤖 Google Gemini
👤 Authentication

Users can create an account and login.

Each user has their own saved articles.

User
 ↓
Login
 ↓
Generate Article
 ↓
Save Article
 ↓
My Articles
📚 Article Management

Saved articles can be:

👀 Viewed
✏️ Edited
🗑️ Deleted

The project uses a Django ForeignKey to connect
articles with users.


⚙️ Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL
cd ai_article_generator

Create a virtual environment:

python -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Create a .env file:

GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key

Run migrations:

python manage.py migrate

Start the server:

python manage.py runserver

Open:

http://127.0.0.1:8000/
🚀 Project Flow
👤 User
  ↓
📝 Enter Topic
  ↓
🌐 Tavily Research
  ↓
🔎 RAG Pipeline
  ↓
🤖 Gemini
  ↓
📄 Generated Article
  ↓
💬 Ask AI
  ↓
💾 Save Article
🎯 What I Learned
🐍 Django fundamentals
👤 Custom User Model
🔗 Django ForeignKey
🗃️ CRUD operations
🌐 API integration
🤖 Generative AI
🦜 LangChain
🔎 RAG
🧠 Embeddings
🗄️ Vector databases
💬 AI conversation memory
🔐 Django sessions
🔮 Future Improvements
🎨 Better UI/UX
📄 Export articles as PDF
📊 Article analytics
☁️ Deployment
⚡ Streaming AI responses

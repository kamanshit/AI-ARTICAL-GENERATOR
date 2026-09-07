# 🤖 AI Article Generator

An AI-powered article generation platform built with **Django** and **Generative AI**.

The application allows users to enter a topic, perform real-time web research, generate a research-based article using **Google Gemini**, chat with the generated article using **RAG**, and save articles to their personal collection.

---

## 🚀 Features

- 🔐 User Registration & Authentication
- 📝 Generate articles from any topic
- 🌐 Real-time web research using Tavily
- ✂️ Intelligent document chunking
- 🧠 Gemini embeddings
- 🗄️ Chroma vector database
- 🔍 Semantic search with Retriever
- 📚 Retrieval-Augmented Generation (RAG)
- 🤖 AI-powered article generation
- 💬 Chat with generated articles
- 🧠 Conversation memory
- 🔗 Display research sources
- 💾 Save generated articles
- 📖 View saved articles
- ✏️ Edit articles
- 🗑️ Delete articles
- 👤 User-specific article collections
- 📱 Responsive UI

---

# 🧠 How The Application Works

The application combines a traditional Django backend with a complete Generative AI pipeline.

The overall architecture looks like this:

```text
                         👤 USER
                           │
                           ▼
                    📝 Enter Article Topic
                           │
                           ▼
                    🌐 Tavily Research
                           │
                           ▼
                     📄 Documents
                           │
                           ▼
                    ✂️ Text Splitting
                           │
                           ▼
                    🧠 Gemini Embeddings
                           │
                           ▼
                    🗄️ Chroma Vector DB
                           │
                           ▼
                       🔍 Retriever
                           │
                           ▼
                    📚 Relevant Context
                           │
                           ▼
                     🤖 Gemini LLM
                           │
                           ▼
                    📄 Generated Article
                           │
                ┌──────────┴──────────┐
                │                     │
                ▼                     ▼
          💬 AI Chat              🔗 Sources
                │
                ▼
          🧠 Chat Memory
                │
                ▼
          💾 Save Article
                │
                ▼
          👤 User's Articles

🏗️ Tech Stack
Backend
🐍 Python
🌐 Django
🗃️ SQLite
🔐 Django Authentication
Generative AI
🤖 Google Gemini
🧩 LangChain
🧠 Gemini Embeddings
🔍 Retrieval-Augmented Generation (RAG)
Research & Vector Search
🌐 Tavily
🗄️ ChromaDB
✂️ RecursiveCharacterTextSplitter
Frontend
HTML
CSS
Django Templates
🌐 Django Backend

Django is responsible for the web application and backend logic.

The project is divided into two main applications:

ai_article_generator/
│
├── articles/
│
└── accounts/
👤 Accounts App

The accounts app handles:

User registration
Login
Logout
Custom user model

The project uses Django's authentication system to manage users.

📝 Articles App

The articles app handles the main application functionality.

It contains:

articles/
├── models.py
├── views.py
├── urls.py
├── forms.py
├── services.py
└── templates/
🗃️ Database Model

The main model is Articles.

class Articles(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    topic = models.CharField(max_length=200)

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

Each article belongs to a specific user.

The relationship is:

User
 │
 ├── Article
 ├── Article
 ├── Article
 └── Article

This allows the application to display each user's own articles.

📝 Article Generation

When the user enters a topic, Django sends the topic to the AI service.

For example:

How is artificial intelligence changing education?

The application then starts the GenAI pipeline.

🌐 Step 1 — Web Research

The application uses Tavily to search the web.

response = tavily_client.search(
    query=self.topic,
    max_results=5
)

The search returns information such as:

Title
URL
Content
Score

Each search result is converted into a LangChain Document.

Document(
    page_content=result.get("content", ""),
    metadata={
        "title": result.get("title"),
        "url": result.get("url")
    }
)

This gives us structured research documents.

✂️ Step 2 — Text Splitting

Large documents are not ideal to send directly into an LLM.

So the research documents are divided into smaller chunks.

The application uses:

RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

Conceptually:

Large Document
       │
       ▼
┌─────────────┐
│ Chunk 1     │
├─────────────┤
│ Chunk 2     │
├─────────────┤
│ Chunk 3     │
├─────────────┤
│ Chunk 4     │
└─────────────┘
Why chunking?

Smaller chunks make it easier for the retriever to find the most relevant information.

The overlap helps preserve context between chunks.

🧠 Step 3 — Embeddings

The application uses Gemini embeddings:

GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

Embeddings convert text into numerical vectors.

For example:

"Artificial intelligence is changing education."
                         │
                         ▼
                  🧠 Embedding
                         │
                         ▼
             [0.016, 0.013, ...]

The resulting vector represents the semantic meaning of the text.

This allows the application to perform semantic search instead of simply matching keywords.

🗄️ Step 4 — Chroma Vector Database

The generated embeddings are stored in Chroma.

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="article_research"
)

Chroma allows the application to search through the research based on semantic similarity.

🔍 Step 5 — Retriever

The vector database is converted into a retriever:

retriever = vectorstore.as_retriever(
    search_kwargs={
        "k": 6
    }
)

When we ask a question:

retriever.invoke(question)

the retriever finds the most relevant chunks.

For example:

Question:
"What are the benefits of AI for teachers?"

              │
              ▼

        🔍 Retriever

              │
       ┌──────┴──────┐
       ▼             ▼
   Chunk 12       Chunk 27
       │             │
       └──────┬──────┘
              ▼
       Relevant Context
🤖 Step 6 — Gemini Article Generation

The retrieved information is provided to Gemini through a structured prompt.

The model is instructed to:

Use the provided research
Avoid inventing facts
Structure the article
Use Markdown
Provide approximately 800 words

The basic flow is:

Retrieved Research
       +
User Topic
       │
       ▼
   Prompt Template
       │
       ▼
    Gemini LLM
       │
       ▼
Generated Article
📚 Retrieval-Augmented Generation (RAG)

RAG is one of the main concepts implemented in this project.

Instead of asking Gemini:

"Write an article about AI in education."

we first retrieve relevant information.

Web Research
     ↓
Documents
     ↓
Chunks
     ↓
Embeddings
     ↓
Chroma
     ↓
Retriever
     ↓
Relevant Context
     ↓
Gemini
     ↓
Answer

This is:

Retrieval-Augmented Generation

The retrieval step provides external context to the LLM before generation.

💬 AI Chatbot

After generating an article, users can ask questions about it.

For example:

User:
What are the benefits for teachers?

AI:
According to the research...

The chatbot also uses RAG.

The article is:

Article
   ↓
Chunks
   ↓
Embeddings
   ↓
Chroma
   ↓
Retriever

Then the user's question retrieves the most relevant sections.

🧠 Conversation Memory

The chatbot also maintains conversation history.

LangChain messages are used:

HumanMessage(
    content=question
)

AIMessage(
    content=answer
)

The conversation is passed back into the prompt using:

MessagesPlaceholder(
    variable_name="chat_history"
)

This allows follow-up questions such as:

User:
What are the benefits of AI in education?

AI:
AI can provide personalized learning...

User:
What about teachers?

AI:
For teachers, AI can...

The second question can use the previous conversation as context.

🔗 Research Sources

The application also displays the sources used during research.

Each source contains:

Title
URL

Users can click the source and visit the original webpage.

This makes the generated article more transparent and research-oriented.

💾 Save Article Workflow

Articles are not saved immediately after generation.

The workflow is:

Generate Article
       ↓
Read Article
       ↓
Ask AI Questions
       ↓
Review Article
       ↓
💾 Save Article
       ↓
Database

When the user clicks Save Article, Django creates an Articles record.

Articles.objects.create(
    user=request.user,
    topic=topic,
    content=article
)
👤 User-Specific Articles

The Home page filters articles using the logged-in user:

Articles.objects.filter(
    user=request.user
)

This means users see their own article collection.

User A
 ├── Article 1
 └── Article 2

User B
 ├── Article 3
 └── Article 4
🧠 Project Architecture

The GenAI logic is separated from Django views.

The main AI logic lives inside:

articles/services.py

The service contains:

ArticleResearch
│
├── search()
│
├── build_retriever()
│
├── retrieve()
│
├── generate_article()
│
└── chat()

This keeps the AI pipeline separate from the Django request/response logic.

📁 Project Structure
ai_article_generator/
│
├── manage.py
├── requirements.txt
├── .gitignore
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── articles/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── services.py
│   │
│   ├── templates/
│   │   └── articles/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── Generate.html
│   │       ├── article_detail.html
│   │       ├── article_update.html
│   │       ├── article_delete.html
│   │       ├── about.html
│   │       └── contact.html
│   │
│   └── static/
│       └── articles/
│           └── style.css
│
└── ai_articale_generator/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
🔐 Environment Variables

API keys are stored inside .env.

GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key

The .env file should never be committed to GitHub.

The project uses:

from dotenv import load_dotenv

load_dotenv()

to load environment variables.

⚙️ Installation
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
cd ai_article_generator
2. Create a virtual environment
python -m venv venv
3. Activate the environment
macOS / Linux
source venv/bin/activate
Windows
venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
5. Create .env

Create a .env file in the project root:

GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
6. Run migrations
python manage.py migrate
7. Start the development server
python manage.py runserver

Open:

http://127.0.0.1:8000/
📦 Requirements

The project uses:

Django
python-dotenv
tavily-python
langchain-core
langchain-text-splitters
langchain-google-genai
langchain-chroma
chromadb
🎯 What I Learned From This Project

This project was built to understand how a real GenAI application can be integrated with a backend framework.

Django
Django project structure
Apps
URLs
Views
Templates
Forms
Models
ForeignKey relationships
Authentication
CRUD operations
Sessions
Generative AI
LLMs
Prompt engineering
LangChain
Web research
Document objects
Text chunking
Embeddings
Vector databases
Semantic search
Retrievers
RAG
Conversation memory
AI-powered chat
🚀 Future Improvements

Possible improvements for future versions:

🎨 More advanced frontend
⚡ Streaming AI responses
✏️ AI-assisted article editing
📊 Article analytics
🔎 Better source management
🗄️ Persistent vector database
🌐 Production deployment
🧪 Automated tests

AI agents and tool-calling are not required for the current version because the application's RAG pipeline already solves its core problem.

🏆 Project Goal

The goal of this project was not simply to call an LLM API.

The goal was to understand how different GenAI components work together inside a real backend application:

Django
  +
Web Research
  +
Embeddings
  +
Vector Database
  +
Retriever
  +
RAG
  +
LLM
  +
Conversation Memory
  =
🤖 AI Article Generator
👨‍💻 Author

Kamanshit

Built as a practical Generative AI + Django project.

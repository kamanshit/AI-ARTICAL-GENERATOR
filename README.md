# 🤖 AI Article Generator

A Django-based AI Article Generator that uses **Google Gemini, Tavily, LangChain, and ChromaDB** to research topics, generate articles, and chat with generated articles.

---

## 🚀 Features

- 👤 User Registration & Login
- 📝 Generate AI Articles
- 🌐 Web Research using Tavily
- 🧠 RAG using ChromaDB
- 💬 Chat with Generated Articles
- 🧠 Conversation Memory
- 🔗 Research Sources
- 💾 Save Articles
- 📖 View Articles
- ✏️ Edit Articles
- 🗑️ Delete Articles
- 🎨 Responsive UI

---

# 🌐 Django Backend

The application is built using **Django**.

Django handles:

- User authentication
- URL routing
- Views
- Forms
- Database models
- Article CRUD operations
- Sessions
- Templates
- Static files

The project contains two main Django apps:

```text
accounts/
articles/
```
👤 Accounts

The accounts app handles:

Registration
Login
Logout
Custom User Model
📝 Articles

The articles app handles:

Article generation
AI chatbot
Article storage
Article detail
Edit
Delete
Web research
🗃️ Database

The application uses SQLite as the database.

Each article is connected to the user who created it using a Django ForeignKey.

User
 ├── Article
 ├── Article
 └── Article

 🤖 Generative AI

The AI functionality is implemented in:

articles/services.py

The project uses:

Google Gemini
LangChain
Tavily
Gemini Embeddings
ChromaDB
🌐 Web Research

When a user enters a topic, the application first searches the web using Tavily.

User Topic
    ↓
Tavily
    ↓
Search Results
    ↓
Documents

The search results are converted into LangChain Document objects.

✂️ Text Splitting

The research documents are split into smaller chunks using:

RecursiveCharacterTextSplitter

The project uses:

chunk_size=500
chunk_overlap=100

This makes the research easier to search and retrieve.

🧠 Embeddings

The project uses Gemini embeddings to convert text into vectors.

Text
 ↓
Gemini Embeddings
 ↓
Vector

This allows the application to perform semantic similarity searches.

🗄️ ChromaDB

The generated embeddings are stored in ChromaDB.

Documents
   ↓
Embeddings
   ↓
ChromaDB

ChromaDB is used as the vector database for the RAG pipeline.

🔍 RAG

The project uses Retrieval-Augmented Generation (RAG).

The basic flow is:

Web Research
     ↓
Documents
     ↓
Text Splitting
     ↓
Embeddings
     ↓
ChromaDB
     ↓
Retriever
     ↓
Relevant Context
     ↓
Google Gemini
     ↓
Generated Article

Instead of sending only the user's topic to Gemini, relevant research is retrieved first and provided as context.

💬 AI Chatbot

After generating an article, users can ask questions about it.

For example:

User:
What are the benefits of AI in education?

AI:
AI can provide personalized learning...

User:
What about teachers?

AI:
AI can also help teachers by...

The chatbot uses the article as its knowledge source and retrieves relevant sections before generating an answer.

🧠 Conversation Memory

The chatbot maintains conversation history using LangChain messages:

HumanMessage
AIMessage

Django sessions are used to maintain the conversation between requests.

This allows the AI to understand follow-up questions.

🔗 Sources

The application displays the sources returned by Tavily.

Each source contains:

Source title
Source URL

Users can click the sources to view the original research.

💾 Save Articles

Articles are not saved immediately after generation.

The workflow is:

Generate Article
      ↓
Chat with Article
      ↓
Review
      ↓
Save Article

Saved articles are stored in the Django database and associated with the logged-in user.

✏️ Article Management

Users can manage their saved articles.

Create
  ↓
Read
  ↓
Update
  ↓
Delete

Users can:

View saved articles
Open article details
Edit articles
Delete articles
🎨 Frontend

The frontend uses:

HTML
Django Templates
CSS

The project uses a single stylesheet:

articles/static/articles/style.css

The UI includes:

Navigation bar
Article cards
Article reader
AI chat interface
Forms
Authentication pages
Source links
Responsive layout
🏗️ Project Structure
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
🛠️ Tech Stack
Backend
🐍 Python
🌐 Django
🗃️ SQLite
Generative AI
🤖 Google Gemini
🧩 LangChain
🧠 Gemini Embeddings
🔍 RAG
Research & Vector Database
🌐 Tavily
🗄️ ChromaDB
Frontend
HTML
CSS
Django Templates
⚙️ Installation
1. Clone the repository
git clone YOUR_REPOSITORY_URL
cd ai_article_generator
2. Create virtual environment
python -m venv venv
3. Activate virtual environment

macOS / Linux:

source venv/bin/activate

Windows:

venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
5. Create .env

Create a .env file in the project root:

GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
6. Run migrations
python manage.py migrate
7. Start the server
python manage.py runserver

Open:

http://127.0.0.1:8000/
🔄 Application Flow

The complete application works like this:

👤 User
   ↓
🌐 Django
   ↓
📝 Enter Topic
   ↓
🌐 Tavily Research
   ↓
✂️ Text Splitting
   ↓
🧠 Gemini Embeddings
   ↓
🗄️ ChromaDB
   ↓
🔍 Retriever
   ↓
🤖 Google Gemini
   ↓
📄 Generated Article
   ↓
💬 AI Chat
   ↓
🧠 Conversation Memory
   ↓
💾 Save Article
   ↓
📚 User's Articles
📚 What I Learned

This project helped me understand how to combine Django with Generative AI.

Django
Project & app structure
URLs
Views
Templates
Forms
Models
ForeignKey
Authentication
Sessions
CRUD
Static files
Generative AI
LLMs
Prompt Engineering
LangChain
Web Research
Document Processing
Text Chunking
Embeddings
Vector Databases
Semantic Search
Retrievers
RAG
Conversation Memory
AI Chatbots
🚀 Future Improvements

Possible future improvements:

⚡ Streaming AI responses
✏️ AI-assisted article editing
📝 Better Markdown rendering
🧪 Automated tests
🌐 Production deployment
📊 Article analytics
👨‍💻 Author

Kamanshit 

Built with:

🐍 Python
🌐 Django
🤖 Generative AI
🧠 RAG
💬 AI Chat

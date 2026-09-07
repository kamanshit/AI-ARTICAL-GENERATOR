# 🤖 AI Article Generator

> A research-powered AI article generation platform built with Django, Google Gemini, Tavily, LangChain, and ChromaDB.

AI Article Generator is a full-stack Generative AI application that allows users to enter a topic, perform real-time web research, generate a research-based article using Google Gemini, chat with the generated article using Retrieval-Augmented Generation (RAG), and save articles to their personal collection.

The project combines a traditional Django backend with a complete Generative AI pipeline to demonstrate how modern AI systems can be integrated into a real web application.

---

## ✨ Features

### 🤖 Generative AI
- Generate articles from user-provided topics
- Google Gemini-powered article generation
- Prompt-based article generation
- Research-grounded responses
- Approximately 800-word article generation

### 🌐 Web Research
- Real-time web research using Tavily
- Multiple search results per topic
- Source title and URL extraction
- Research-backed article generation

### 🧠 RAG Pipeline
- Document creation using LangChain
- Recursive text splitting
- Gemini embeddings
- ChromaDB vector store
- Semantic retrieval
- Context-aware generation

### 💬 AI Chatbot
- Chat with generated articles
- Ask follow-up questions
- Retrieval-Augmented responses
- Conversation memory
- Human and AI message history

### 👤 User System
- User registration
- Login
- Logout
- Custom user model
- User-specific article collections

### 📚 Article Management
- Generate articles
- View saved articles
- View article details
- Edit articles
- Delete articles
- Save articles only after reviewing/chatting

### 🎨 UI
- Responsive interface
- Clean article cards
- Article reading layout
- AI chat interface
- Source section
- Authentication pages
- Consistent styling using a single CSS file

---

# 🏗️ Tech Stack

## Backend

- 🐍 Python
- 🌐 Django
- 🗃️ SQLite
- 🔐 Django Authentication

## Generative AI

- 🤖 Google Gemini
- 🧩 LangChain
- 🧠 Gemini Embeddings
- 🔎 Retrieval-Augmented Generation (RAG)

## Research & Retrieval

- 🌐 Tavily
- 🗄️ ChromaDB
- ✂️ RecursiveCharacterTextSplitter

## Frontend

- HTML
- CSS
- Django Templates

---

# 🧠 System Architecture

The application follows this overall architecture:

```text
                         👤 USER
                           │
                           ▼
                  📝 Enter Article Topic
                           │
                           ▼
                    🌐 Tavily Search
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
                    🗄️ ChromaDB
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
                    📄 AI Article
                           │
                ┌──────────┴──────────┐
                │                     │
                ▼                     ▼
           💬 AI Chat             🔗 Sources
                │
                ▼
        🧠 Conversation Memory
                │
                ▼
          💾 Save Article
                │
                ▼
         👤 User's Collection

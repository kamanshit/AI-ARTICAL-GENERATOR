import os

from dotenv import load_dotenv

from tavily import TavilyClient

from langchain_core.documents import Document
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)
from langchain_core.messages import (
    HumanMessage,
    AIMessage
)

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI
)

from langchain_chroma import Chroma


load_dotenv()


# =========================
# Models / Clients
# =========================

tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)


model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)


# =========================
# Article Prompt
# =========================

article_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an expert research-based article writer.

        Write an accurate, informative and engaging article
        using ONLY the research context provided.

        Do not invent facts.

        If the research does not provide enough information
        for a claim, do not make that claim.

        Structure the article with:

        - A clear title
        - Introduction
        - Well-organized sections
        - Examples where useful
        - Conclusion

        Use Markdown formatting.

        Write approximately 800 words.

        Research context:

        {context}
        """
    ),
    (
        "human",
        """
        Write an article about:

        {topic}
        """
    )
])


article_chain = article_prompt | model


# =========================
# Chat Prompt
# =========================

chat_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an AI research assistant.

        The user is discussing this topic:

        {topic}

        Answer using the research context and
        conversation history.

        Do not invent facts.

        If the research does not contain enough
        information, say so.

        Research context:

        {context}
        """
    ),

    MessagesPlaceholder(
        variable_name="chat_history"
    ),

    (
        "human",
        "{question}"
    )
])


chat_chain = chat_prompt | model


# =========================
# Article Research
# =========================

class ArticleResearch:

    def __init__(self, topic):

        self.topic = topic

        self.chat_history = []

        self.documents = []

        self.chunks = []

        self.vectorstore = None

        self.retriever = None


    # =========================
    # Search
    # =========================

    def search(self):

        response = tavily_client.search(
            query=self.topic,
            max_results=5
        )

        for result in response["results"]:

            document = Document(
                page_content=result.get("content", ""),
                metadata={
                    "title": result.get("title"),
                    "url": result.get("url")
                }
            )

            self.documents.append(document)


    # =========================
    # Build Vector Store
    # =========================

    def build_retriever(self):

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )

        self.chunks = text_splitter.split_documents(
            self.documents
        )


        self.vectorstore = Chroma.from_documents(
            documents=self.chunks,
            embedding=embeddings,
            collection_name="article_research"
        )


        self.retriever = self.vectorstore.as_retriever(
            search_kwargs={
                "k": 6
            }
        )


    # =========================
    # Retrieve Research
    # =========================

    def retrieve(self, question):

        return self.retriever.invoke(question)


    # =========================
    # Generate Article
    # =========================

    def generate_article(self):

        retrieved_documents = self.retrieve(
            self.topic
        )


        context = "\n\n".join(
            document.page_content
            for document in retrieved_documents
        )


        response = article_chain.invoke({
            "context": context,
            "topic": self.topic
        })


        article = response.content[0]["text"]


        sources = []

        for document in retrieved_documents:

            source = {
                "title": document.metadata.get("title"),
                "url": document.metadata.get("url")
            }

            if source not in sources:
                sources.append(source)


        return {
            "article": article,
            "sources": sources
        }


    # =========================
    # Chat
    # =========================

    def chat(self, question):

        retrieved_documents = self.retrieve(
            question
        )


        context = "\n\n".join(
            document.page_content
            for document in retrieved_documents
        )


        response = chat_chain.invoke({
            "topic": self.topic,
            "context": context,
            "chat_history": self.chat_history,
            "question": question
        })


        answer = response.content[0]["text"]


        self.chat_history.append(
            HumanMessage(
                content=question
            )
        )


        self.chat_history.append(
            AIMessage(
                content=answer
            )
        )


        return answer



# =========================
# Generate Article Function
# =========================

def generate_articles(topic):

    research = ArticleResearch(topic)

    research.search()

    research.build_retriever()

    return research.generate_article()

# =========================
# Article Chat
# =========================

def chat_with_article(topic, article, question, chat_history):
    
    document = Document(
        page_content=article,
        metadata={
            "topic": topic
        }
    )

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = text_splitter.split_documents(
        [document]
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name="article_chat"
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={
            "k": 4
        }
    )

    retrieved_documents = retriever.invoke(question)

    context = "\n\n".join(
        document.page_content
        for document in retrieved_documents
    )

    response = chat_chain.invoke({
        "topic": topic,
        "context": context,
        "chat_history": chat_history,
        "question": question
    })

    return response.content[0]["text"]
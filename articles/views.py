from django.shortcuts import render, redirect
from .services import generate_articles
from .models import Articles
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from .services import generate_articles, chat_with_article
from langchain_core.messages import HumanMessage, AIMessage

@login_required
def home(request):
    articles = Articles.objects.filter(
        user = request.user
    )
    data={
        'articles':articles
    }
    return render(request, "articles/home.html", data)

@login_required
@login_required
@login_required
def generateArticle(request):

    if request.method == "POST":

        form = ArticleForm(request.POST)

        if form.is_valid():

            topic = form.cleaned_data["topic"]

            result = generate_articles(topic)

            article = result["article"]
            sources = result["sources"]

            # Store topic in session
            request.session["article_topic"] = topic

            # Start a fresh chat
            request.session.pop("chat_history", None)

            return render(
                request,
                "articles/Generate.html",
                {
                    "form": form,
                    "article": article,
                    "sources": sources,
                    "topic": topic
                }
            )

    else:
        form = ArticleForm()

    return render(
        request,
        "articles/Generate.html",
        {
            "form": form
        }
    )

@login_required
def article_chat(request):

    if request.method == "POST":

        topic = request.POST.get("topic")
        article = request.POST.get("article")
        question = request.POST.get("question")

        # Get previous chat history
        chat_history = request.session.get("chat_history", [])

        # Convert session data into LangChain messages
        messages = []

        for message in chat_history:

            if message["role"] == "human":
                messages.append(
                    HumanMessage(
                        content=message["content"]
                    )
                )

            elif message["role"] == "ai":
                messages.append(
                    AIMessage(
                        content=message["content"]
                    )
                )

        # Ask the AI
        answer = chat_with_article(
            topic,
            article,
            question,
            messages
        )

        # Save conversation in session
        chat_history.append({
            "role": "human",
            "content": question
        })

        chat_history.append({
            "role": "ai",
            "content": answer
        })

        request.session["chat_history"] = chat_history

        return render(
            request,
            "articles/Generate.html",
            {
                "topic": topic,
                "article": article,
                "question": question,
                "answer": answer,
                "chat_history": chat_history
            }
        )

    return redirect("generateArticle")

@login_required
def save_article(request):

    if request.method == "POST":

        topic = request.session.get("article_topic")
        article = request.POST.get("article")

        Articles.objects.create(
            user=request.user,
            topic=topic,
            content=article
        )

        # Clear temporary article data
        request.session.pop("article_topic", None)
        request.session.pop("chat_history", None)

        return redirect("home")

    return redirect("generateArticle")

def article_list(request):
    articles = Articles.objects.all()
    return render(
        request, "articles/article_list.html",{"articles":articles}
    )
@login_required
def article_detail(request, id):
    article = Articles.objects.get(
        id=id,
        user = request.user
        )
    return render(
        request, "articles/article_detail.html",{"article": article}
    )
@login_required
def article_update(request, id):
    article = Articles.objects.get(id=id, user=request.user)

    if request.method == "POST":
        form = ArticleForm(request.POST)

        if form.is_valid():
            article.topic = form.cleaned_data["topic"]
            article.save()

            return render(
                request,
                "articles/article_detail.html",
                {"article": article}
            )

    else:
        form = ArticleForm(initial={
            "topic": article.topic
        })

    return render(
        request,
        "articles/article_update.html",
        {
            "form": form,
            "article": article
        }
    )
@login_required
def article_delete(request, id):
    article = Articles.objects.get(id=id, user = request.user)
    if request.method=='POST':
        article.delete()

        return redirect("home")

    return render(
        request, "articles/article_delete.html", {"article":article}
    )

    
    
        


def about(request):
    return render(request, "articles/about.html")


def contact(request):
    return render(request, "articles/contact.html")
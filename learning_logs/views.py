
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic, Entry


def index(request):
    topics = Topic.objects.all()
    context = {"topics": topics}
    return render(request, "learning_logs/index.html", context)


def topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)

    if request.method == "POST":
        text = request.POST.get("text", "").strip()

        if text:
            Entry.objects.create(topic=topic, text=text)

        return HttpResponseRedirect(
            reverse("topic", args=[topic.id])
        )

    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)


def new_topic(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()

        if name:
            Topic.objects.create(text=name)
            return redirect("index")

    return render(request, "learning_logs/new_topic.html")

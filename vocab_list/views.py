from django.views.generic import DetailView, ListView

from .models import VocabularyList


class VocabularyListListView(ListView):

    template_name = "vocab_list/list.html"
    model = VocabularyList


class VocabularyListDetailView(DetailView):

    template_name = "vocab_list/detail.html"
    model = VocabularyList
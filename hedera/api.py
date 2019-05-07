import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from lattices.models import LatticeNode
from lattices.utils import get_or_create_nodes_for_form_and_lemmas
from lemmatized_text.models import LemmatizedText
from vocab_list.models import (
    PersonalVocabularyList,
    PersonalVocabularyListEntry,
    PersonalVocabularyStats,
    VocabularyList,
    VocabularyListEntry
)


class APIView(View):

    def get_data(self):
        return {}

    def render_to_response(self):
        return JsonResponse({"data": self.get_data()})

    def get(self, request, *args, **kwargs):
        return self.render_to_response()


class LemmatizedTextDetailAPI(APIView):

    def get_data(self):
        text = get_object_or_404(LemmatizedText, pk=self.kwargs.get("pk"))
        return text.api_data()


class LemmatizationAPI(APIView):

    def decorate_token_data(self, text):
        data = text.data
        if self.request.GET.get("vocablist", None) is not None:
            vl = get_object_or_404(VocabularyList, pk=self.request.GET.get("vocablist"))
            nodes = LatticeNode.objects.filter(pk__in=[token["node"] for token in data])
            for token in data:
                node = nodes.filter(pk=token["node"]).first()  # does doing this avoid a second trip to the database?
                if node is not None:
                    token["inVocabList"] = token["resolved"] and vl.entries.filter(node__in=node.related_nodes()).exists()
                else:
                    token["inVocabList"] = False

        if self.request.GET.get("personalvocablist", None) is not None:
            vl = get_object_or_404(PersonalVocabularyList, pk=self.request.GET.get("personalvocablist"))
            for token in data:
                token["inVocabList"] = token["resolved"] and vl.entries.filter(node__pk=token["node"]).exists()
                token["familiarity"] = token["resolved"] and vl.node_familiarity(token["node"])

        # add glosses - probably a better way
        entries = {
            entry.node.id: entry.gloss
            for entry in VocabularyListEntry.objects.filter(node__id__in=[t["node"] for t in data])
        }
        for token in data:
            token["gloss"] = entries.get(token["node"], None)

        return data

    def get_data(self):
        text = get_object_or_404(LemmatizedText, pk=self.kwargs.get("pk"))
        data = self.decorate_token_data(text)
        return data

    def post(self, request, *args, **kwargs):
        text = get_object_or_404(LemmatizedText, pk=self.kwargs.get("pk"))
        data = json.loads(request.body)
        token_index = data["tokenIndex"]
        node_id = data["nodeId"]
        resolved = data["resolved"]

        text_data = text.data

        if node_id is None:
            form = text_data[token_index]["token"]
            node_id = get_or_create_nodes_for_form_and_lemmas(form, [data["lemma"]], context="user").pk

        text_data[token_index]["node"] = node_id
        text_data[token_index]["resolved"] = resolved
        text.data = text_data
        text.save()

        text.refresh_from_db()
        data = self.decorate_token_data(text)
        return JsonResponse({"data": data})


class VocabularyListAPI(APIView):

    def get_data(self):
        return [v.data() for v in VocabularyList.objects.filter(lang=self.request.GET.get("lang"))]


class PersonalVocabularyListAPI(APIView):

    @property
    def text(self):
        if getattr(self, "_text", None) is None:
            self._text = get_object_or_404(LemmatizedText, pk=self.request.GET.get("text"))
        return self._text

    def get_object(self):
        vl, _ = PersonalVocabularyList.objects.get_or_create(
            user=self.request.user,
            lang=self.text.lang,
        )
        return vl

    def get_data(self):
        vl = self.get_object()
        return dict(
            personalVocabList=vl.data(),
            unknownGlosses=None
        )

    def post(self, request, *args, **kwargs):
        vl = self.get_object()

        data = json.loads(request.body)
        familiarity = int(data["familiarity"])

        pk = kwargs.get("pk", None)
        if pk is not None:
            entry = get_object_or_404(PersonalVocabularyListEntry, pk=pk)
            entry.familiarity = familiarity
            entry.save()
        else:
            node = get_object_or_404(LatticeNode, pk=data["nodeId"])
            headword = data["headword"]
            gloss = data["gloss"]
            vl.entries.create(
                headword=headword,
                gloss=gloss,
                familiarity=familiarity,
                node=node,
            )

        stats, _ = PersonalVocabularyStats.objects.get_or_create(text=self.text, vocab_list=vl)
        stats.update()

        vl.refresh_from_db()

        return JsonResponse({"data": vl.data()})

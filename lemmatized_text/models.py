from django.db import models


# this is for representing the lemmatized text

class LemmatizedText(models.Model):

    title = models.CharField(max_length=100)
    lang = models.CharField(max_length=3)  # ISO 639.2

    # this should be a JSON list of the form
    # [
    #   {"token": "res publica", "node": 1537, "resolved": true},
    #   {"token": "est", "node": 42, "resolved": false},
    #   ...
    # ]
    # where node is the pk of the LatticeNode

    data = models.TextField()

    def __str__(self):
        return self.title

    def api_data(self):
        return {
            "id": self.pk,
            "title": self.title,
            "lang": self.lang,
        }

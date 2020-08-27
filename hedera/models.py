from django.db import models

from django.contrib.auth.models import User


SHOW_NODE_CHOICES = [
    ("always", "Always show node id"),
    ("never", "Never show node id"),
    ("toggle", "Let me toggle the reveal of node ids"),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=250, blank=True)
    show_node_ids = models.CharField(max_length=10, choices=SHOW_NODE_CHOICES, default="never")

    def __str__(self):
        return self.display_name or self.user.email

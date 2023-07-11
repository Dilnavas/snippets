from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Snippet, Tag


class SnippetSerializer(serializers.ModelSerializer):
    tag = serializers.PrimaryKeyRelatedField(
        required=True, queryset=Tag.objects.all(), many=False
    )
    user = serializers.PrimaryKeyRelatedField(
        required=True, queryset=User.objects.all(), many=False
    )
    title = serializers.CharField(required=True)
    snippet = serializers.CharField(required=True)

    class Meta:
        model = Snippet
        fields = ["tag", "user", "snippet", "title"]

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Tag, Snippet
from .serializers import SnippetSerializer


class Snippets(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, snippet_id=None):
        try:
            if snippet_id:
                try:
                    snippet = Snippet.objects.get(id=snippet_id)
                    return Response(
                        {
                            "status": "success",
                            "data": {
                                "user": snippet.user.username,
                                "tag": snippet.tag.title,
                                "snippet": snippet.snippet,
                                "title": snippet.title,
                                "created_at": snippet.created_at,
                            },
                        },
                        status=status.HTTP_200_OK,
                    )
                except Snippet.DoesNotExist:
                    return Response(
                        {"status": "error", "data": "Requested snippet doesn't exist"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                snippets = Snippet.objects.all()
                return Response(
                    {
                        "status": "success",
                        "total": len(snippets),
                        "data": [
                            {"title": snippet.title, "link": f"{request.build_absolute_uri()}{snippet.id}"}
                            for snippet in snippets
                        ],
                    },
                    status=status.HTTP_200_OK,
                )
        except Exception as _e:
            return Response(
                {"status": "error", "data": str(_e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def post(self, request):
        try:
            data = request.data
            if "tag" in data:
                try:
                    tag = Tag.objects.get(title=data["tag"])
                except Tag.DoesNotExist:
                    tag = Tag()
                    tag.title = data["tag"]
                    tag.save()
                data["tag"] = tag.id
            data["user"] = request.user.id
            serializer = SnippetSerializer(data=data)
            if serializer.is_valid():
                snippet = serializer.save()
                return Response(
                    {
                        "status": "success",
                        "data": {
                            "user": snippet.user.username,
                            "tag": snippet.tag.title,
                            "snippet": snippet.snippet,
                            "title": snippet.title,
                            "created_at": snippet.created_at,
                        },
                    },
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"status": "error", "data": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as _e:
            return Response(
                {"status": "error", "data": str(_e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def put(self, request, snippet_id):
        try:
            data = request.data
            data["user"] = request.user.id
            if "tag" in data:
                try:
                    tag = Tag.objects.get(title=data["tag"])
                except Tag.DoesNotExist:
                    tag = Tag()
                    tag.title = data["tag"]
                    tag.save()
                data["tag"] = tag.id
            serializer = SnippetSerializer(data=data)
            if serializer.is_valid():
                try:
                    snippet = Snippet.objects.get(id=snippet_id)
                    snippet.tag = tag
                    snippet.user = request.user
                    snippet.title = data["title"]
                    snippet.snippet = data["snippet"]
                    snippet.save()
                    return Response(
                        {
                            "status": "success",
                            "data": {
                                "user": snippet.user.username,
                                "tag": snippet.tag.title,
                                "snippet": snippet.snippet,
                                "title": snippet.title,
                                "created_at": snippet.created_at,
                            },
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                except Snippet.DoesNotExist:
                    return Response(
                        {"status": "error", "data": "Requested snippet doesn't exist"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(
                    {"status": "error", "data": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as _e:
            return Response(
                {"status": "error", "data": str(_e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def delete(self, request, snippet_id):
        try:
            snippet = Snippet.objects.get(id=snippet_id)
            snippet.delete()
            return Response(
                {
                    "status": "success",
                    "data": {
                        "user": snippet.user.username,
                        "tag": snippet.tag.title,
                        "snippet": snippet.snippet,
                        "title": snippet.title,
                        "created_at": snippet.created_at,
                    },
                },
                status=status.HTTP_200_OK,
            )
        except Exception as _e:
            return Response(
                {"status": "error", "data": str(_e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class Tags(APIView):
    permission_classes = (IsAuthenticated,)

    def get(slef, request, tag_title=None):
        try:
            if tag_title:
                snippets = Snippet.objects.filter(tag__title=tag_title)
                return Response(
                    {
                        "status": "success",
                        "data": [
                            {
                                "user": snippet.user.username,
                                "tag": snippet.tag.title,
                                "snippet": snippet.snippet,
                                "title": snippet.title,
                                "created_at": snippet.created_at,
                            }
                            for snippet in snippets
                        ],
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                tags = Tag.objects.all()
                return Response(
                    {
                        "status": "success",
                        "data": [
                            {
                                "title": tag.title,
                                "created_at": tag.created_at,
                            }
                            for tag in tags
                        ],
                    },
                    status=status.HTTP_200_OK,
                )
        except Exception as _e:
            return Response(
                {"status": "error", "data": str(_e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

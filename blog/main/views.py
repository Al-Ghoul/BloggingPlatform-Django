from rest_framework import (
    viewsets,
    permissions,
    status,
    exceptions,
    generics,
    filters,
)
from rest_framework.response import Response
from .serializers import PostSerializer, UserSerializer
from .models import Post
from rest_framework.pagination import CursorPagination

class PostCursorSetPagination(CursorPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    ordering = '-created_at'


class UserViewSet(viewsets.ViewSet):
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == "create" or self.action == "destroy":
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content", "category"]
    pagination_class = PostCursorSetPagination


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.save(author=request.user, raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        post = generics.get_object_or_404(self.queryset, pk=pk)
        if post.author != request.user:
            raise exceptions.PermissionDenied()
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk=None):
        post = generics.get_object_or_404(self.queryset, pk=pk)
        if post.author != request.user:
            raise exceptions.PermissionDenied()
        serializer = self.serializer_class(post, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update(post, serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

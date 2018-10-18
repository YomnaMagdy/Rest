from django.db.models import Q
from rest_framework.filters import(
SearchFilter,
OrderingFilter
)
from rest_framework.generics import (
ListAPIView,
RetrieveAPIView,
UpdateAPIView,
DestroyAPIView,
CreateAPIView,
)
from rest_framework.permissions import(
AllowAny,
IsAuthenticated,
IsAdminUser,
IsAuthenticatedOrReadOnly,#for making permissions for user

)
from.pagination import limitOffset,OurPageNumberPagination
from posts.models import Post

from .serializers import(
PostCreateSerializer,
PostListSerializer,
PostDetailSerializer,
)
from .permissions import IsOwnerOrReadOnly


class PostListAPIview(ListAPIView):
    serializer_class = PostListSerializer
    filter_backends=[SearchFilter]
    search_fields=['title','content','user__first_name']
    pagination_class = OurPageNumberPagination
    def get_queryset(self, *args, **kwargs):

        queryset_list= Post.objects.all()
        query = request.GET.get("q")
        if query :
    		queryset_list = queryset_list.filter(
    		Q(title__icontains=query)|
    		Q(content__icontains=query)|
    		Q(user__first_name__icontains=query) |
    		Q(user__last_name__icontains=query)
    		).distinct()
        return queryset_List


class PostDetailAPIview(RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field ='slug'

class PostUpdateAPIview(UpdateAPIView):
    queryset=Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field ='slug'
    permission_classes=[IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def perform_updated(self,serializer):
        serializer.save(user=self.request.user)

class PostDeleteAPIview(DestroyAPIView):
    queryset=Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field ='slug'

class PostCreateAPIview(CreateAPIView):
    queryset=Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes=[IsAuthenticated]
def perform_create(self,serializer):
    serializer.save(user=self.request.user)

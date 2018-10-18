from rest_framework.serializers import(
 ModelSerializer,
 HYperlinkedIdentityField,
 SerializerMethodField,
 )
from posts.models import Post

class PostListSerializer(ModelSerializer):
    url=HyperLinkedIdentityField(
    view_name='posts-api:detail'
    lookup_field='slug'
    )
    class Meta:
        model=Post
        fields=(
        'url'
        'id',
        'title',
        'slug',
        'content',
        )
class PostDetailSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields=(
        'id',
        'title',
        'slug',
        'content',
        )
class PostCreateSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields=(
        'title',
        'content',
        'publish'
        )

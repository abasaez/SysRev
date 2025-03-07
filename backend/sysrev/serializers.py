from rest_framework import serializers
from .models import Tag

class TagSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ['id', 'name', 'description', 'parent_tag', 'children']

#recursively obtains children for each tag
    def get_children(self, obj):
        serializer = TagSerializer(obj.child_tags.all(), many=True)
        return serializer.data
'''
A Serializer class to serialize and deserialize the snippet instances into representations such as `json`.

DRF - Django Rest Framework - an extension of django, provides serializers that work very similar to django forms:

1. Converts complex data types(querysets or model instances) into Python data types that can be easily rendered into JSON or XML.
2. Like Django forms, serializers in DRF also handle validation. When accepting data from a client, the serializer ensures the data
    is valid according to the rules we've set.
3. It can also deserialize.
'''

from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Each field on the serializer represents a field on the Snippet model.
    They define how the data should be serialized and deserialized.
    '''
    # Refactored Code
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id','highlight', 'title','owner', 'code', 'lineos', 'language', 'style']


class UserSerializer(serializers.ModelSerializer):

    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    queryset = Snippet.objects.all()

    class Meta:
        model = User
        fields = ['url','id', 'username', 'snippets']
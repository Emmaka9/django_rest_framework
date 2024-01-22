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

class SnippetSerializer(serializers.ModelSerializer):
    '''
    Each field on the serializer represents a field on the Snippet model.
    They define how the data should be serialized and deserialized.
    '''

    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required = False, allow_blank=True, max_length=100)
    # code = serializers.CharField(style={'base_template': 'textarea.html'})
    # lineos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')


    # def create(self, validated_data):
    #     """
    #     Create and return a new Snippet instance, given the validated data.
    #     """

    #     return Snippet.objects.create(**validated_data)
    

    # def update(self, instance, validated_data):
    #     '''
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     '''
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.lineos = validated_data.get('lineos', instance.lineos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()

    #     return instance

    # ------------------------------------------------------------------------------------------
    # Refactored Code
    
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'lineos', 'language', 'style']
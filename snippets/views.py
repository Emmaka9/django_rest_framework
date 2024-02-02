'''
Refactor!!
REST framework provides a set of already mixed-in generic views that can be used to trim down our views.py module even more.
'''

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User

class SnippetList(generics.ListCreateAPIView):
    
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

'''
Add read-only views for the user representations. Use ListAPIView and RetrieveAPIView generic class.
'''
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



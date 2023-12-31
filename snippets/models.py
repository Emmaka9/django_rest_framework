from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles



'''
A simple snippet model that is used to store code snippets.
'''

# Each item is a tuple with multiple elements
# the second item of this tuple is a list of aliases for the lexer.
# the condition filters out lexers without aliases
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(i[1][0] , i[0]) for i in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    lineos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)


class Meta:
    ordering = ['created']
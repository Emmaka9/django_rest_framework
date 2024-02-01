from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight



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
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    lineos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    def save(self, *args, **kwargs):
        '''
        Use the `pygments` library to create a highlighted HTML representation of the code snippet.
        '''

        lexer = get_lexer_by_name(self.language)
        lineos = 'table' if self.lineos else False
        options = {'title': self.title} if self.title else False
        formatter = HtmlFormatter(style=self.style, lineos = lineos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)


class Meta:
    ordering = ['created']
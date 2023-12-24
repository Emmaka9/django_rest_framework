from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
l = [i for i in get_all_lexers()]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

l1_len = len(l)
l2_len = len(LEXERS)
print(l1_len, l2_len)
x = 10

# for i in range(10):
#     print(f'l[{x+i}]: {l[x+i]}')

# print('-'*100)
# for i in range(10):
#     print(f'L2[{x+i}]: {LEXERS[X+i]}')

print(STYLE_CHOICES)
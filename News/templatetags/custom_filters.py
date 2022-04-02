from django import template


register = template.Library()


CURRENCIES_SYMBOLS = {
   'IT': '*I',
}


@register.filter()
def currency(value, code='IT'):

   postfix = CURRENCIES_SYMBOLS[code]

   return f'{value} {postfix}'
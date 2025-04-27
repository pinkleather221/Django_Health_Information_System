from django import template

register = template.Library()

@register.filter(name='attr')
def attr(field, args):
    """
    Adds attributes to form field widget.
    Usage: {{ field|attr:"class:form-control" }}
    """
    attrs = {}
    for arg in args.split(','):
        key, value = arg.split(':')
        attrs[key.strip()] = value.strip()
    return field.as_widget(attrs=attrs)

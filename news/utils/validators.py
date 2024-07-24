from django.forms import ValidationError


def validate_title(value):
    if len(value.split()) < 2:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")


""" def validate_news(value):
    if len(value.split()) == 0:
         """

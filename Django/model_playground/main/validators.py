from django.core.exceptions import ValidationError
#here i create my custom validators. OO this is fun

def validate_even_number(value):
    if value % 2:
        raise ValidationError("Given Value is not even")
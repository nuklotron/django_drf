from rest_framework.exceptions import ValidationError


class UrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        allowed = ['youtube.com']
        tmp_val = dict(value).get(self.field)
        if tmp_val.lower():
            for k in allowed:
                if k in tmp_val.lower():
                    break

                else:
                    raise ValidationError("Prohibited video URL provided")

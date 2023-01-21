# Third Party Stuff
from rest_framework.renderers import JSONRenderer


class WebcastApiRenderer(JSONRenderer):
    media_type = "application/vnd.webcast+json"

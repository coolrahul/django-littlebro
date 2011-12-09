import anyjson
from littlebro.backends.base import BaseBackend
from littlebro.apps.events.models import Event

class SimpleBackend(BaseBackend):
    """
    Backend to save event records to default littlebro_events database table.
    Should be used primarily for testing.
    """
    def __init__(self, *args, **kwargs):
        BaseBackend.__init__(self, *args, **kwargs)
        
    def save(self, event, params={}, collection=None):
        """
        Save event to database.
        """
        Event.objects.create(event=event, params=anyjson.serialize(params))
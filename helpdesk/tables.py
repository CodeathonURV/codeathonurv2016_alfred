import django_tables2 as tables
from helpdesk.models import *

class TopicsTable(tables.Table):
    class Meta:
        model = Topic

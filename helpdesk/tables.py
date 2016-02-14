import django_tables2 as tables
from helpdesk.models import *
from django_tables2.utils import A

class ReceivedTopicsTable(tables.Table):
    title = tables.LinkColumn('topic', args=[A('pk')])
    class Meta:
        model = Topic
        fields = ('creation_date', 'title', 'autor', 'status', 'is_public', 'last_update' )

class SentTopicsTable(tables.Table):
    title = tables.LinkColumn('topic', args=[A('pk')])
    class Meta:
        model = Topic
        fields = ('creation_date', 'title', 'receiver', 'status', 'is_public', 'last_update' )

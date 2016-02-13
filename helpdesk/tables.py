import django_tables2 as tables
from helpdesk.models import *
from django_tables2.utils import A

class TopicsTable(tables.Table):
    title = tables.LinkColumn('student_topic', args=[A('pk')])
    class Meta:
        model = Topic
        fields = ('creation_date', 'title', 'author', 'status', 'is_public', 'last_update' )

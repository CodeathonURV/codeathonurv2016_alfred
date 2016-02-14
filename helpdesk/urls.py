from django.conf.urls import url

from . import views

urlpatterns = [
   # post views,
    url(r'^pdi/$', views.pdi_topics, name='pdi_topics_home'),
    url(r'^pas/$', views.pas_topics, name='pas_topics_home'),
    url(r'^student/$', views.get_queryset, name='student_ask_faq_home'),

    url(r'^search/$', views.get_queryset, name='search'),
    url(r'^pdi/topics/$', views.pdi_topics, name='pdi_topics'),
    url(r'^pas/topics/$', views.pas_topics, name='pas_topics'),
    url(r'^student/topics/$', views.student_topics, name='student_topics'),

    url(r'^topics/(?P<topic_id>[0-9]+)/$', views.topic, name='topic'),
    url(r'^topics/(?P<topic_id>[0-9]+)/comment/$', views.topic_comment, name='topic_comment'),
    url(r'^topics/(?P<topic_id>[0-9]+)/close/$', views.topic_close, name='topic_close'),

    url(r'^pdi/ask_faq/$', views.get_queryset, name='pdi_ask_faq'),
    url(r'^pas/ask_faq/$', views.get_queryset, name='pas_ask_faq'),
    url(r'^student/ask_faq/$', views.get_queryset, name='student_ask_faq'),

    url(r'^ranking/$', views.ranking, name='ranking'),

    url(r'^pdi/profile/(?P<pk>[0-9]+)/$', views.pdi_profile, name='pdi_profile'),
    url(r'^pas/profile/(?P<pk>[0-9]+)/$', views.pas_profile, name='pas_profile'),
    url(r'^student/profile/(?P<pk>[0-9]+)/$', views.student_profile, name='student_profile'),

    url(r'^pdi/ask/$', views.pdi_new_topic_for_pas, name='pdi_new_topic'),
    url(r'^pas/ask/$', views.pas_new_topic_for_pas, name='pas_new_topic'),
    url(r'^student/ask/pas/$', views.student_new_topic_for_pas, name='student_new_topic_pas'),
    url(r'^student/ask/pdi/$', views.student_new_topic_for_pdi, name='student_new_topic_pdi'),

    url(r'^pdi/ask/employee/$', views.pdi_choose_pas, name='pdi_choose_employee'),
    url(r'^pas/ask/employee/$', views.pas_choose_pas, name='pas_choose_employee'),
    url(r'^student/ask/pdi/teacher/$', views.student_choose_teacher, name='student_choose_teacher'),
    url(r'^student/ask/pas/employee/$', views.student_choose_pas, name='student_choose_pas'),

    url(r'^vote/$', views.vote_comment, name='vote_comment'),

]

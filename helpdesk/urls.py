from django.conf.urls import url

from . import views

urlpatterns = [
   # post views,
    url(r'^pdi/$', views.pdi_topics, name='pdi_topics_home'),
    url(r'^pas/$', views.pas_topics, name='pas_topics_home'),
    url(r'^student/$', views.student_ask_faq, name='student_ask_faq_home'),

    url(r'^pdi/topics/$', views.pdi_topics, name='pdi_topics'),
    url(r'^pas/topics/$', views.pas_topics, name='pas_topics'),
    url(r'^student/topics/$', views.student_topics, name='student_topics'),

    url(r'^pdi/topics/(?P<topic_id>[0-9]+)$', views.pdi_topic, name='pdi_topic'),
    url(r'^pas/topics/(?P<topic_id>[0-9]+)$', views.pas_topic, name='pas_topic'),
    url(r'^student/topics/(?P<topic_id>[0-9]+)$', views.student_topic, name='student_topic'),

    url(r'^pdi/ask_faq/$', views.pdi_ask_faq, name='pdi_ask_faq'),
    url(r'^pas/ask_faq/$', views.pas_ask_faq, name='pas_ask_faq'),
    url(r'^student/ask_faq/$', views.student_ask_faq, name='student_ask_faq'),

    url(r'^pdi/ranking/$', views.pdi_ranking, name='pdi_ranking'),
    url(r'^pas/ranking/$', views.pas_ranking, name='pas_ranking'),

    url(r'^pdi/profile/(?P<pk>\d+)/$', views.pdi_profile, name='pdi_profile'),
    url(r'^pas/profile/(?P<pk>\d+)/$', views.pas_profile, name='pas_profile'),
    url(r'^student/profile/(?P<pk>\d+)/$', views.student_profile, name='student_profile'),

    url(r'^pdi/ask/$', views.pdi_new_topic_for_pas, name='pdi_new_topic'),
    url(r'^pas/ask/$', views.pas_new_topic_for_pas, name='pas_new_topic'),
    url(r'^student/ask/pas/$', views.student_new_topic_for_pas, name='student_new_topic_pas'),
    url(r'^student/ask/pdi/$', views.student_new_topic_for_pdi, name='student_new_topic_pdi'),

]

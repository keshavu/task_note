
from django.conf.urls import url
from django.views.generic import TemplateView
from task.views import CreateNote, ListNote, DeleteNote

urlpatterns = [
    # url(r'^about/$', TemplateView.as_view(template_name="about.html")),
    url(r'^create/$', CreateNote.as_view(), name='create'),
    url(r'^$', ListNote.as_view(), name='list'),

    url(r'^delete/(?P<pk>\d+)/$', DeleteNote.as_view(), name='delete'),

]
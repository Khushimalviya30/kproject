from django.conf.urls import url
from todo.views import about,contact,addreviews,allreviews,service,todoedit,tododelete

urlpatterns=[
    url(r'^$',allreviews,name='allreviews'),
    url(r'^add/$',addreviews,name='addreviews'),
    url(r'^about/$',about,name='about'),
    url(r'^contact/$',contact,name='contact'),
    url(r'^service/$',service,name='service'),
    url(r'^edit/(?P<pk>\d+)/$',todoedit,name='todoedit'),
    url(r'^delete/(?P<pk>\d+)/$',tododelete,name='tododelete'),

]
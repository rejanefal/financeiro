from django.conf.urls import include, url
from django.contrib import admin


admin.site.site_header = ('Sistema Financeiro')
admin.site.index_title = ('Menu')
admin.site.site_title = ('Sistema Financeiro')


urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('financas.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
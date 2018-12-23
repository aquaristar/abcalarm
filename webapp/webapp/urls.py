from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^abcalarm/', include('abcalarm.urls', namespace='abcalarm')),
    url(r'^$', RedirectView.as_view(url='abcalarm')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

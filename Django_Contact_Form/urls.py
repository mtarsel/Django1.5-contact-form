from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django_Contact_Form.views.home', name='home'),
    # url(r'^Django_Contact_Form/', include('Django_Contact_Form.foo.urls')),
    url(r'^thankyou/', controllers.thankyou),
    url(r'^contact/', 'contact.views.contact'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

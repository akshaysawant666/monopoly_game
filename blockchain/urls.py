from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/', include('blockchain.api.urls'), name='api'),
]

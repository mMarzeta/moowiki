from django.conf.urls import url

from movie_picker.fuzzy.views import user_input


urlpatterns = [
    url(r'^$', user_input, name='user_input'),
]

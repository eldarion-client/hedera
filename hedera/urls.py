from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path

from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls

from lti.views import LtiInitializerView, LtiRegistrationView

from . import api, views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("django-rq/", include("django_rq.urls")),
    re_path(r"^account/", include("account.urls")),

    path("read/<int:text_id>/", views.read, name="read"),

    path("lemmatized_text/", include("lemmatized_text.urls")),
    path("lattices/", include("lattices.urls")),
    path("vocab/", include("vocab_list.urls")),

    path("classes/", include("groups.urls")),

    path("api/v1/lemmatized_texts/", api.LemmatizedTextListAPI.as_view()),
    path("api/v1/lemmatized_texts/<int:pk>/detail/", api.LemmatizedTextDetailAPI.as_view()),
    path("api/v1/lemmatized_texts/<int:pk>/status/", api.LemmatizedTextStatusAPI.as_view()),
    path("api/v1/lemmatized_texts/<int:pk>/<str:action>/", api.LemmatizedTextStatusAPI.as_view()),
    path("api/v1/lemmatized_texts/<int:pk>/", api.LemmatizationAPI.as_view()),
    path("api/v1/vocab_lists/", api.VocabularyListAPI.as_view()),
    path("api/v1/vocab_lists/<int:pk>/entries/", api.VocabularyListEntriesAPI.as_view()),
    path("api/v1/vocab_entries/<int:pk>/link/", api.VocabularyListEntryAPI.as_view()),
    path("api/v1/personal_vocab_list/", api.PersonalVocabularyListAPI.as_view()),
    path("api/v1/personal_vocab_list/<int:pk>/", api.PersonalVocabularyListAPI.as_view()),

    path("lti/", include("lti_provider.urls")),
    path("lti/lti_initializer/", LtiInitializerView.as_view(), name="lti_initializer"),
    path("lti/lti_registration", LtiRegistrationView.as_view(), name="lti_registration"),

    path("cms/", include(wagtailadmin_urls)),
    re_path(r"", include(wagtail_urls)),

] + static(
    settings.STATIC_URL, document_root=settings.STATIC_URL
) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

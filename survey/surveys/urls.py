from django.conf.urls import url
from survey.surveys import views as survey_views

urlpatterns = [
    url(
        r'^$',
        survey_views.SurveyListView.as_view(),
        name='survey-list'
    ),
    url(
        r'^(?P<pk>[0-9]+)/instructions',
        survey_views.SurveyInstructionView.as_view(),
        name='survey-instructions'
    ),
    url(
        r'^(?P<pk>[0-9]+)/practice',
        survey_views.SurveyPracticeView.as_view(),
        name='survey-practice'
    ),
    url(
        r'^(?P<pk>[0-9]+)',
        survey_views.SurveyView.as_view(),
        name='survey'
    ),
]

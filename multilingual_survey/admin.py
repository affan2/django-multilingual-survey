"""Admin classes for the multilingual_survey app."""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from generic_positions.admin import GenericPositionsAdmin
from hvad.admin import TranslatableAdmin

from .models import Survey, SurveyQuestion, SurveyAnswer, SurveyResponse
from .forms import SurveyResponseAdminForm


class SurveyAdmin(TranslatableAdmin):
    """Custom admin for the ``Survey`` model."""
    list_display = ['id', 'get_title', 'slug']

    save_on_top = True

    readonly_fields = ('id', 'created', 'created_by', 'updated', 'updated_by')

    def get_title(self, obj):
        return obj.__str__()
    get_title.short_description = _('Title')

    def save_form(self, request, form, change):
        f = super(SurveyAdmin, self).save_form(request, form, change)
        if not f.pk:
            f.created_by = request.user
        else:
            f.updated_by = request.user

        return f

    def get_fieldsets(self, request, obj=None):
        return (
            (None, {'fields': ['id', 'title', 'description']}),
            ('Additional Information', {'classes': ('collapse',), 'fields': ['created', 'created_by',
                                                                             'updated', 'updated_by']}),
        )


class SurveyQuestionAdmin(GenericPositionsAdmin, TranslatableAdmin):
    """Custom admin for the ``SurveyQuestion`` model."""
    list_display = ['get_title', 'get_survey', 'slug', 'is_choice_field', 'is_multi_select',
                    'has_other_field', 'required']

    save_on_top = True

    readonly_fields = ('id', 'created', 'created_by', 'updated', 'updated_by')

    def get_title(self, obj):
        return obj.__str__()
    get_title.short_description = _('Title')

    def get_survey(self, obj):
        return obj.survey
    get_survey.short_description = _('Survey')

    def save_form(self, request, form, change):
        f = super(SurveyQuestionAdmin, self).save_form(request, form, change)
        if not f.pk:
            f.created_by = request.user
        else:
            f.updated_by = request.user

        return f

    def get_fieldsets(self, request, obj=None):
        return (
            (None, {'fields': ['id', 'title', 'content', 'survey', 'is_choice_field', 'is_multi_select',
                        'has_other_field', 'required']}),
            ('Additional Information', {'classes': ('collapse',), 'fields': ['created', 'created_by',
                                                                             'updated', 'updated_by']}),
        )


class SurveyAnswerAdmin(GenericPositionsAdmin, TranslatableAdmin):
    """Custom admin for the ``SurveyAnswer`` model."""
    list_display = ['get_title', 'slug', 'get_question']

    save_on_top = True

    readonly_fields = ('id', 'created', 'updated')

    def get_title(self, obj):
        return obj.__str__()
    get_title.short_description = _('Title')

    def get_question(self, obj):
        return obj.question
    get_question.short_description = _('Question')

    def save_form(self, request, form, change):
        f = super(SurveyAnswerAdmin, self).save_form(request, form, change)
        if not f.pk:
            f.created_by = request.user
        else:
            f.updated_by = request.user

        return f

    def get_fieldsets(self, request, obj=None):
        return (
            (None, {'fields': ['id', 'title', 'question']}),
            ('Additional Information', {'classes': ('collapse',), 'fields': ['created', 'updated', ]}),
        )


class SurveyResponseAdmin(admin.ModelAdmin):
    """Custom admin for the ``SurveyResponse`` model."""
    list_display = ['user_email', 'question', 'get_answer', 'created']

    save_on_top = True

    readonly_fields = ('id', 'created', 'updated', 'user', 'session_id')

    fieldsets = [
        (None, {'fields': ['id', 'user', 'session_id', 'question', 'answer', 'other_answer',]}),
        ('Additional Information', {'classes': ('collapse',), 'fields': ['created', 'updated', ]}),
    ]

    form = SurveyResponseAdminForm

    def get_answer(self, obj):
        answer_string = ''
        for answer in obj.answer.all():
            if answer_string == '':
                answer_string += answer.__str__()
            else:
                answer_string += u', {0}'.format(answer.__str__())
        if obj.other_answer:
            if answer_string == '':
                answer_string += obj.other_answer
            else:
                answer_string += u', *{0}'.format(obj.other_answer)
        return answer_string[:30]
    get_answer.short_description = _('Answer')

    def user_email(self, obj):
        return obj.user.email if obj.user else 'Anonymous'
    user_email.short_description = _('User')

    def save_form(self, request, form, change):
        f = super(SurveyResponseAdmin, self).save_form(request, form, change)
        if not f.pk:
            f.created_by = request.user
        else:
            f.updated_by = request.user

        return f


admin.site.register(SurveyResponse, SurveyResponseAdmin)
admin.site.register(SurveyAnswer, SurveyAnswerAdmin)
admin.site.register(SurveyQuestion, SurveyQuestionAdmin)
admin.site.register(Survey, SurveyAdmin)

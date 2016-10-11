# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SurveyResponseUserDetails'
        db.create_table(u'multilingual_survey_surveyresponseuserdetails', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('job_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'multilingual_survey', ['SurveyResponseUserDetails'])

        # Adding field 'Survey.created'
        db.add_column(u'multilingual_survey_survey', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2016, 10, 10, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Survey.created_by'
        db.add_column(u'multilingual_survey_survey', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name=u'multilingual_survey_survey_created_by', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Survey.updated'
        db.add_column(u'multilingual_survey_survey', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2016, 10, 10, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Survey.updated_by'
        db.add_column(u'multilingual_survey_survey', 'updated_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'multilingual_survey_survey_updated_by', null=True, to=orm['auth.User']),
                      keep_default=False)


        # Changing field 'Survey.slug'
        db.alter_column(u'multilingual_survey_survey', 'slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=200, populate_from='title', unique_with=()))
        # Adding field 'SurveyQuestion.created'
        db.add_column(u'multilingual_survey_surveyquestion', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2016, 10, 10, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'SurveyQuestion.created_by'
        db.add_column(u'multilingual_survey_surveyquestion', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name=u'multilingual_survey_surveyquestion_created_by', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'SurveyQuestion.updated'
        db.add_column(u'multilingual_survey_surveyquestion', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2016, 10, 10, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'SurveyQuestion.updated_by'
        db.add_column(u'multilingual_survey_surveyquestion', 'updated_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'multilingual_survey_surveyquestion_updated_by', null=True, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'SurveyQuestion.is_choice_field'
        db.add_column(u'multilingual_survey_surveyquestion', 'is_choice_field',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'SurveyQuestion.slug'
        db.alter_column(u'multilingual_survey_surveyquestion', 'slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=200, populate_from='title'))
        # Adding field 'SurveyAnswer.created'
        db.add_column(u'multilingual_survey_surveyanswer', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2016, 10, 10, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'SurveyAnswer.updated'
        db.add_column(u'multilingual_survey_surveyanswer', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2016, 10, 10, 0, 0), blank=True),
                      keep_default=False)


        # Changing field 'SurveyAnswer.slug'
        db.alter_column(u'multilingual_survey_surveyanswer', 'slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=200, populate_from='title'))
        # Deleting field 'SurveyResponse.date_created'
        db.delete_column(u'multilingual_survey_surveyresponse', 'date_created')

        # Adding field 'SurveyResponse.user_details'
        db.add_column(u'multilingual_survey_surveyresponse', 'user_details',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='responses', null=True, to=orm['multilingual_survey.SurveyResponseUserDetails']),
                      keep_default=False)

        # Adding field 'SurveyResponse.created'
        db.add_column(u'multilingual_survey_surveyresponse', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2016, 10, 10, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'SurveyResponse.updated'
        db.add_column(u'multilingual_survey_surveyresponse', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2016, 10, 10, 0, 0), blank=True),
                      keep_default=False)


        # Changing field 'SurveyQuestionTranslation.title'
        db.alter_column(u'multilingual_survey_surveyquestion_translation', 'title', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'SurveyAnswerTranslation.title'
        db.alter_column(u'multilingual_survey_surveyanswer_translation', 'title', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Deleting model 'SurveyResponseUserDetails'
        db.delete_table(u'multilingual_survey_surveyresponseuserdetails')

        # Deleting field 'Survey.created'
        db.delete_column(u'multilingual_survey_survey', 'created')

        # Deleting field 'Survey.created_by'
        db.delete_column(u'multilingual_survey_survey', 'created_by_id')

        # Deleting field 'Survey.updated'
        db.delete_column(u'multilingual_survey_survey', 'updated')

        # Deleting field 'Survey.updated_by'
        db.delete_column(u'multilingual_survey_survey', 'updated_by_id')


        # Changing field 'Survey.slug'
        db.alter_column(u'multilingual_survey_survey', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=255, unique=True))
        # Deleting field 'SurveyQuestion.created'
        db.delete_column(u'multilingual_survey_surveyquestion', 'created')

        # Deleting field 'SurveyQuestion.created_by'
        db.delete_column(u'multilingual_survey_surveyquestion', 'created_by_id')

        # Deleting field 'SurveyQuestion.updated'
        db.delete_column(u'multilingual_survey_surveyquestion', 'updated')

        # Deleting field 'SurveyQuestion.updated_by'
        db.delete_column(u'multilingual_survey_surveyquestion', 'updated_by_id')

        # Deleting field 'SurveyQuestion.is_choice_field'
        db.delete_column(u'multilingual_survey_surveyquestion', 'is_choice_field')


        # Changing field 'SurveyQuestion.slug'
        db.alter_column(u'multilingual_survey_surveyquestion', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=255))
        # Deleting field 'SurveyAnswer.created'
        db.delete_column(u'multilingual_survey_surveyanswer', 'created')

        # Deleting field 'SurveyAnswer.updated'
        db.delete_column(u'multilingual_survey_surveyanswer', 'updated')


        # Changing field 'SurveyAnswer.slug'
        db.alter_column(u'multilingual_survey_surveyanswer', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=255))
        # Adding field 'SurveyResponse.date_created'
        db.add_column(u'multilingual_survey_surveyresponse', 'date_created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2016, 10, 10, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'SurveyResponse.user_details'
        db.delete_column(u'multilingual_survey_surveyresponse', 'user_details_id')

        # Deleting field 'SurveyResponse.created'
        db.delete_column(u'multilingual_survey_surveyresponse', 'created')

        # Deleting field 'SurveyResponse.updated'
        db.delete_column(u'multilingual_survey_surveyresponse', 'updated')


        # Changing field 'SurveyQuestionTranslation.title'
        db.alter_column(u'multilingual_survey_surveyquestion_translation', 'title', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'SurveyAnswerTranslation.title'
        db.alter_column(u'multilingual_survey_surveyanswer_translation', 'title', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        u'actstream.action': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'Action'},
            'action_object_content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'action_object'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'action_object_object_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'actor_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'actor'", 'to': u"orm['contenttypes.ContentType']"}),
            'actor_object_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'batch_time_minutes': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_batchable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'state': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'target_content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'target'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'target_object_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'timestamp_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'verb': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'relationships': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_to'", 'symmetrical': 'False', 'through': u"orm['relationships.Relationship']", 'to': u"orm['auth.User']"}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'generic_positions.objectposition': {
            'Meta': {'object_name': 'ObjectPosition'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'multilingual_survey.survey': {
            'Meta': {'unique_together': '()', 'object_name': 'Survey', 'index_together': '()'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'multilingual_survey_survey_created_by'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '200', 'populate_from': "'title'", 'unique_with': '()'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'multilingual_survey_survey_updated_by'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'multilingual_survey.surveyanswer': {
            'Meta': {'unique_together': "(('slug', 'question'),)", 'object_name': 'SurveyAnswer', 'index_together': '()'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['multilingual_survey.SurveyQuestion']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '200', 'populate_from': "'title'"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'multilingual_survey.surveyanswertranslation': {
            'Meta': {'unique_together': "(('language_code', 'master'),)", 'object_name': 'SurveyAnswerTranslation', 'db_table': "u'multilingual_survey_surveyanswer_translation'", 'index_together': '()'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['multilingual_survey.SurveyAnswer']"}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'multilingual_survey.surveyquestion': {
            'Meta': {'unique_together': "(('slug', 'survey'),)", 'object_name': 'SurveyQuestion', 'index_together': '()'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'multilingual_survey_surveyquestion_created_by'", 'to': u"orm['auth.User']"}),
            'has_other_field': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_choice_field': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_multi_select': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '200', 'populate_from': "'title'"}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questions'", 'to': u"orm['multilingual_survey.Survey']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'multilingual_survey_surveyquestion_updated_by'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'multilingual_survey.surveyquestiontranslation': {
            'Meta': {'unique_together': "(('language_code', 'master'),)", 'object_name': 'SurveyQuestionTranslation', 'db_table': "u'multilingual_survey_surveyquestion_translation'", 'index_together': '()'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['multilingual_survey.SurveyQuestion']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'multilingual_survey.surveyresponse': {
            'Meta': {'ordering': "('question',)", 'object_name': 'SurveyResponse'},
            'answer': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'responses'", 'symmetrical': 'False', 'to': u"orm['multilingual_survey.SurveyAnswer']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other_answer': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'responses'", 'null': 'True', 'to': u"orm['multilingual_survey.SurveyQuestion']"}),
            'session_id': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'responses'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_details': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'responses'", 'null': 'True', 'to': u"orm['multilingual_survey.SurveyResponseUserDetails']"})
        },
        u'multilingual_survey.surveyresponseuserdetails': {
            'Meta': {'object_name': 'SurveyResponseUserDetails'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'multilingual_survey.surveytranslation': {
            'Meta': {'unique_together': "(('language_code', 'master'),)", 'object_name': 'SurveyTranslation', 'db_table': "u'multilingual_survey_survey_translation'", 'index_together': '()'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2048', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['multilingual_survey.Survey']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'relationships.relationship': {
            'Meta': {'ordering': "('created',)", 'unique_together': "(('from_user', 'to_user', 'status', 'site'),)", 'object_name': 'Relationship'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_users'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'relationships'", 'to': u"orm['sites.Site']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['relationships.RelationshipStatus']"}),
            'to_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_users'", 'to': u"orm['auth.User']"}),
            'weight': ('django.db.models.fields.FloatField', [], {'default': '1.0', 'null': 'True', 'blank': 'True'})
        },
        u'relationships.relationshipstatus': {
            'Meta': {'ordering': "('name',)", 'object_name': 'RelationshipStatus'},
            'from_slug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'symmetrical_slug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'to_slug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'verb': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['multilingual_survey']

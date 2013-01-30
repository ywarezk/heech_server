# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Drive'
        db.create_table('heech_server_app_drive', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 30, 0, 0))),
            ('modified_data', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 30, 0, 0), auto_now=True, blank=True)),
            ('user_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['heech_server_app.UserProfile'], unique=True)),
            ('drive_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 30, 0, 0))),
            ('origin', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('destination', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(default='0.00', max_digits=6, decimal_places=3)),
        ))
        db.send_create_signal('heech_server_app', ['Drive'])


    def backwards(self, orm):
        # Deleting model 'Drive'
        db.delete_table('heech_server_app_drive')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'heech_server_app.drive': {
            'Meta': {'object_name': 'Drive'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 30, 0, 0)'}),
            'destination': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'drive_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 30, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_data': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 30, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '6', 'decimal_places': '3'}),
            'user_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['heech_server_app.UserProfile']", 'unique': 'True'})
        },
        'heech_server_app.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 30, 0, 0)'}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'facebook_link': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'facebook_username': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'modified_data': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 30, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': "orm['auth.User']"})
        },
        'heech_server_app.usersetting': {
            'Meta': {'object_name': 'UserSetting'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 30, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_notify_similar_driver': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_notify_similar_passenger': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_data': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 30, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'search_radius': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['heech_server_app.UserProfile']", 'unique': 'True'})
        }
    }

    complete_apps = ['heech_server_app']
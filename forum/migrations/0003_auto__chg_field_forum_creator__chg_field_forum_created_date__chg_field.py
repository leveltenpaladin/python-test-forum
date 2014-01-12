# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Forum.creator'
        db.alter_column(u'forum_forum', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forum.ForumUser']))

        # Changing field 'Forum.created_date'
        db.alter_column(u'forum_forum', 'created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Reply.user'
        db.alter_column(u'forum_reply', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forum.ForumUser']))

        # Changing field 'Reply.created_date'
        db.alter_column(u'forum_reply', 'created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Thread.created_date'
        db.alter_column(u'forum_thread', 'created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Thread.op'
        db.alter_column(u'forum_thread', 'op_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forum.ForumUser']))

    def backwards(self, orm):

        # Changing field 'Forum.creator'
        db.alter_column(u'forum_forum', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Forum.created_date'
        db.alter_column(u'forum_forum', 'created_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Reply.user'
        db.alter_column(u'forum_reply', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Reply.created_date'
        db.alter_column(u'forum_reply', 'created_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Thread.created_date'
        db.alter_column(u'forum_thread', 'created_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Thread.op'
        db.alter_column(u'forum_thread', 'op_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

    models = {
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'forum.forum': {
            'Meta': {'object_name': 'Forum'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_forums'", 'to': u"orm['forum.ForumUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_forums'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['forum.Forum']"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'forum.forumuser': {
            'Meta': {'object_name': 'ForumUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'forum.reply': {
            'Meta': {'object_name': 'Reply'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'replies'", 'to': u"orm['forum.Thread']"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forum.ForumUser']"})
        },
        u'forum.thread': {
            'Meta': {'object_name': 'Thread'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'op': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forum.ForumUser']"}),
            'parent_forum': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'threads'", 'to': u"orm['forum.Forum']"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['forum']
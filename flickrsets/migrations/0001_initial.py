# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'RegisteredSet'
        db.create_table('flickrsets_registered_set', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flickr_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
        ))
        db.send_create_signal('flickrsets', ['RegisteredSet'])

        # Adding model 'Person'
        db.create_table('flickrsets_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flickr_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('realname', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('photos_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('profile_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('mobile_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('icon_server', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('icon_farm', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(default='X', max_length=1, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('photos_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('flickrsets', ['Person'])

        # Adding model 'Photoset'
        db.create_table('flickrsets_photoset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photosets', to=orm['flickrsets.Person'])),
            ('primary', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photoset_primaries', to=orm['flickrsets.Photo'])),
            ('flickr_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('server', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('farm', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('photos_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('flickrsets', ['Photoset'])

        # Adding model 'Tag'
        db.create_table('flickrsets_photo_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tags', to=orm['flickrsets.Person'])),
            ('flickr_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('raw', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('flickrsets', ['Tag'])

        # Adding model 'Photo'
        db.create_table('flickrsets_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photoset', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='photos', null=True, to=orm['flickrsets.Photoset'])),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photos', to=orm['flickrsets.Person'])),
            ('flickr_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('server', self.gf('django.db.models.fields.IntegerField')()),
            ('farm', self.gf('django.db.models.fields.IntegerField')()),
            ('license', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('media', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('secret', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('original_secret', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('original_format', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('views_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('comments_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('date_uploaded', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date_posted', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date_taken', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('flickrsets', ['Photo'])

        # Adding M2M table for field tags on 'Photo'
        db.create_table('flickrsets_photo_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photo', models.ForeignKey(orm['flickrsets.photo'], null=False)),
            ('tag', models.ForeignKey(orm['flickrsets.tag'], null=False))
        ))
        db.create_unique('flickrsets_photo_tags', ['photo_id', 'tag_id'])

        # Adding model 'ExifTag'
        db.create_table('flickrsets_exif_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='exif_tags', to=orm['flickrsets.Photo'])),
            ('tag_space', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tag_space_id', self.gf('django.db.models.fields.IntegerField')()),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('raw', self.gf('django.db.models.fields.TextField')()),
            ('clean', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('flickrsets', ['ExifTag'])


    def backwards(self, orm):
        
        # Deleting model 'RegisteredSet'
        db.delete_table('flickrsets_registered_set')

        # Deleting model 'Person'
        db.delete_table('flickrsets_person')

        # Deleting model 'Photoset'
        db.delete_table('flickrsets_photoset')

        # Deleting model 'Tag'
        db.delete_table('flickrsets_photo_tag')

        # Deleting model 'Photo'
        db.delete_table('flickrsets_photo')

        # Removing M2M table for field tags on 'Photo'
        db.delete_table('flickrsets_photo_tags')

        # Deleting model 'ExifTag'
        db.delete_table('flickrsets_exif_tag')


    models = {
        'flickrsets.exiftag': {
            'Meta': {'object_name': 'ExifTag', 'db_table': "'flickrsets_exif_tag'"},
            'clean': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'exif_tags'", 'to': "orm['flickrsets.Photo']"}),
            'raw': ('django.db.models.fields.TextField', [], {}),
            'tag_space': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tag_space_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'flickrsets.person': {
            'Meta': {'object_name': 'Person'},
            'flickr_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'X'", 'max_length': '1', 'blank': 'True'}),
            'icon_farm': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'icon_server': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mobile_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photos_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'photos_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'profile_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'realname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'flickrsets.photo': {
            'Meta': {'object_name': 'Photo'},
            'comments_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'date_posted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_uploaded': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'farm': ('django.db.models.fields.IntegerField', [], {}),
            'flickr_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'media': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'original_format': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'original_secret': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photos'", 'to': "orm['flickrsets.Person']"}),
            'photoset': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photos'", 'null': 'True', 'to': "orm['flickrsets.Photoset']"}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'server': ('django.db.models.fields.IntegerField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'photos'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['flickrsets.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'views_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'flickrsets.photoset': {
            'Meta': {'object_name': 'Photoset'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'farm': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'flickr_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photosets'", 'to': "orm['flickrsets.Person']"}),
            'photos_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'primary': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photoset_primaries'", 'to': "orm['flickrsets.Photo']"}),
            'server': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'flickrsets.registeredset': {
            'Meta': {'object_name': 'RegisteredSet', 'db_table': "'flickrsets_registered_set'"},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'flickr_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'flickrsets.tag': {
            'Meta': {'object_name': 'Tag', 'db_table': "'flickrsets_photo_tag'"},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tags'", 'to': "orm['flickrsets.Person']"}),
            'flickr_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'raw': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['flickrsets']

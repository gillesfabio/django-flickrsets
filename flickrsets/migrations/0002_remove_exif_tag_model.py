# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'ExifTag'
        db.delete_table('flickrsets_exif_tag')

        # Adding field 'Photo._exif'
        db.add_column('flickrsets_photo', '_exif', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'ExifTag'
        db.create_table('flickrsets_exif_tag', (
            ('raw', self.gf('django.db.models.fields.TextField')()),
            ('tag_space', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('clean', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='exif_tags', to=orm['flickrsets.Photo'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag_space_id', self.gf('django.db.models.fields.IntegerField')()),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('flickrsets', ['ExifTag'])

        # Deleting field 'Photo._exif'
        db.delete_column('flickrsets_photo', '_exif')


    models = {
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
            '_exif': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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

"""
Django Flickrsets application ``fsets`` command.
"""
import sys

from django.core.management.base import BaseCommand

from prettytable import PrettyTable

from flickrsets import settings as app_settings
from flickrsets import synchronizer
from flickrsets.client import FlickrClient
from flickrsets.models import RegisteredSet

COMMAND_ARGS = {
    'sync': 'Synchronizes registered Flickr sets with Flickr.',
    'list': 'Lists all registered Flickr sets.',
    'add': 'Registers a new Flickr set for synchronization.',
    'remove': 'Removes (deletes) a registered Flickr set.',
    'enable': 'Enables a disabled Flickr set.',
    'disable': 'Disables an enabled Flickr set.',
    'settings': 'Displays application settings',
}


class Command(BaseCommand):
    """
    The ``fsets`` command.
    """
    help = "Manage Flickr sets of Django Flickrsets application."

    def handle(self, *args, **options):
        """
        Handles the command.
        """
        if len(args) > 0:
            cmd = args[0]
            if cmd not in COMMAND_ARGS:
                sys.stderr.write(
                    ('fsets command only accepts these arguments: '
                     '%s\n' % ', '.join(COMMAND_ARGS.keys())),
                )
                return
            if len(args) > 1:
                cmd_arg = args[1]
                if cmd_arg == 'help':
                    sys.stderr.write('%s\n' % COMMAND_ARGS[cmd])
                    return
                else:
                    sys.stderr.write(
                        ('fsets "%s" argument only accepts "help"'
                        ' options. Other ones will be ignored.'
                        '\n' % cmd_arg),
                    )
                    return
        else:
            sys.stderr.write(
                ('fsets command accepts these arguments:'
                 ' %s\n' % ', '.join(COMMAND_ARGS.keys())),
            )
            return
        cmd = args[0]
        cmd_method = getattr(self, 'fsets_%s' % cmd)
        cmd_method()

    def fsets_sync(self):
        """
        Synchronizes Flickr sets.
        """
        client = FlickrClient(app_settings.FLICKR_API_KEY)
        synchronizer.run(client)

    def fsets_settings(self):
        """
        Displays application settings.
        """
        table = PrettyTable()
        table.field_names = ["Key", "Value"]
        table.align["Key"] = "l"
        table.align["Value"] = "l"
        settings = (
            'FLICKR_API_KEY',
            'FLICKR_USER_ID',
            'CREATE_TAGS',
            'CREATE_EXIF_TAGS',
            'EXIF_TAG_SPACE_LIST',
            'PERSON_LIST_VIEW_PAGINATE_BY',
            'PHOTO_LIST_VIEW_PAGINATE_BY',
            'PHOTOSET_LIST_VIEW_PAGINATE_BY',
            'TAG_LIST_VIEW_PAGINATE_BY',
            'SYNCHRONIZER_PHOTO_TIME_SLEEP',
            'SYNCHRONIZER_PHOTOSET_TIME_SLEEP',
        )
        for setting in settings:
            table.add_row([
                'FLICKRSETS_%s' % setting,
                getattr(app_settings, setting),
            ])
        print table.get_string()

    def fsets_list(self):
        """
        Lists all registered Flickr sets.
        """
        items = self.get_items(remote=False)
        self.print_items(items)

    def fsets_add(self):
        """
        Registers a new Flickr set.
        """
        items = self.get_items(remote=True)
        user_items = self.get_user_items("add", items)
        info = []
        for item in user_items:
            title, flickr_id = item[0], item[1]
            obj, created = RegisteredSet.objects.get_or_create(
                flickr_id=flickr_id,
                title=title)
            if created:
                print 'Added set "%s" (%s).' % (title, flickr_id)
            else:
                print 'Set "%s" (%s) already registered.' % (title, flickr_id)

    def fsets_remove(self):
        """
        Removes a Flickr set.
        """
        items = self.get_items(remote=False)
        user_items = self.get_user_items("remove", items)
        for item in user_items:
            title, flickr_id = item[0], item[1]
            RegisteredSet.objects.get(flickr_id=flickr_id).delete()
            print 'Removed set %s (%s).' % (title, flickr_id)

    def fsets_enable(self):
        """
        Enables a Flickr set.
        """
        items = self.get_items(remote=False, status_filter='disabled')
        user_items = self.get_user_items("enable", items)
        for item in user_items:
            title, flickr_id = item[0], item[1]
            obj = RegisteredSet.objects.get(flickr_id=flickr_id)
            obj.enabled = True
            obj.save()
            print 'Set %s (%s) is enabled.' % (title, flickr_id)

    def fsets_disable(self):
        """
        Disables a Flickr set.
        """
        items = self.get_items(remote=False, status_filter='enabled')
        user_items = self.get_user_items("disable", items)
        for item in user_items:
            title, flickr_id = item[0], item[1]
            obj = RegisteredSet.objects.get(flickr_id=flickr_id)
            obj.enabled = False
            obj.save()
            print 'Set %s (%s) is disabled.' % (title, flickr_id)

    def print_items(self, items):
        """
        Prints items
        """
        table = PrettyTable()
        table.field_names = ["ID", "Title", "Flickr ID", "Status"]
        table.align["ID"] = "r"
        table.align["Title"] = "l"
        table.align["Flickr ID"] = "r"
        table.align["Status"] = "c"
        for idx, title, flickr_id, status in items:
            table.add_row([str(idx), title, flickr_id, status])
        print table.get_string()

    def get_remote_items(self):
        """
        Returns set list from Flickr API.
        """
        client = FlickrClient(app_settings.FLICKR_API_KEY)
        json = client.photosets.getList(user_id=app_settings.FLICKR_USER_ID)
        items = json.get('photosets').get('photoset')
        return [
            (idx, item.get('title').get('_content'), item.get('id'), "REMOTE")
            for idx, item in enumerate(items)]

    def get_db_items(self, status_filter=None):
        """
        Returns set list from database.
        """
        items = RegisteredSet.objects.all()
        if status_filter == 'enabled':
            items = RegisteredSet.objects.enabled()
        if status_filter == 'disabled':
            items = RegisteredSet.objects.disabled()

        def status_msg(boolean):
            if boolean:
                return "ENABLED"
            return "DISABLED"

        return [
            (idx, item.title, item.flickr_id, status_msg(item.enabled))
            for idx, item in enumerate(items)]

    def get_items(self, remote=False, status_filter=None):
        """
        Returns a list of sets from Flickr API or database.
        """
        if remote:
            items = self.get_remote_items()
        else:
            items = self.get_db_items(status_filter)
        if not items:
            print 'No set available.'
            sys.exit()
        return items

    def get_user_items(self, verb, items):
        """
        Displays the ``verb`` in the question sent to the user and returns a
        list of tuples containing items title and Flickr ID, by extracting
        them from ``items``.

        Example of returned value::

            [('Super Set', '19879872'), ('Other Set', '2890820398')]

        """
        self.print_items(items)
        try:
            choices = raw_input(
                ("\nWhich Flickr set(s) you want to %s? " % str(verb)))
        except KeyboardInterrupt:
            sys.exit()
        if not choices:
            sys.exit()
        choices = choices.replace(',', '').split(' ')
        try:
            int_choices = []
            for choice in choices:
                int_choices.append(int(choice))
        except ValueError:
            sys.exit()
        user_items = []
        for choice in int_choices:
            user_items.append((items[choice][1], items[choice][2]))
        return user_items

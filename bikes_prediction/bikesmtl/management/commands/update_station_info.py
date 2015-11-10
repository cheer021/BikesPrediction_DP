from django.core.management.base import BaseCommand, CommandError
from bikesmtl.models import Station
import urllib
from lxml import etree

class Command(BaseCommand):
    help = 'Updates station info (name and location)'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        Station.objects.all().delete()
        dataNowMtl = urllib.urlopen('http://montreal.bixi.com/data/bikeStations.xml')

        root = etree.parse(dataNowMtl)
        for ele in root.xpath("//stations/station"):
            if ele.xpath("installed")[0].text == "true" and ele.xpath("locked")[0].text == "false":
                s = Station(station_id = int(ele.xpath("id")[0].text), name = ele.xpath("name")[0].text, latitude = float(ele.xpath("lat")[0].text), longitude = float(ele.xpath("long")[0].text))
                s.save()
        self.stdout.write('Successfully updated station info')
                
        # for poll_id in options['poll_id']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write('Successfully closed poll "%s"' % poll_id)
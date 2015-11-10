from django.core.management.base import BaseCommand, CommandError
from bikesmtl.models import Station, StationDataNow
from django.utils import timezone
import datetime
import urllib
from lxml import etree

class Command(BaseCommand):
    help = 'Updates station info (name and location)'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        dataNowMtl = urllib.urlopen('http://montreal.bixi.com/data/bikeStations.xml')
        root = etree.parse(dataNowMtl)

        if (len(StationDataNow.objects.all()) == 0): empty = True;
        else: empty = False;

        lastUpdate = datetime.datetime.utcfromtimestamp(int(int(root.xpath("//stations")[0].get("LastUpdate"))/1000))
        lastUpdate = timezone.make_aware(lastUpdate)
        for ele in root.xpath("//stations/station"):
            if ele.xpath("installed")[0].text == "true" and ele.xpath("locked")[0].text == "false":
                # station = StationDataNow(station = Station.objects.filter(station_id = int(ele.xpath("id")[0].text))[0], nb_bikes = int(ele.xpath("nbBikes")[0].text), nb_empty_docks = int(ele.xpath("nbEmptyDocks")[0].text), datetime = timezone.now(), last_comm_with_server = lastUpdate)
                # station.save()
                if (empty):
                    s = StationDataNow(station = Station.objects.get(station_id = int(ele.xpath("id")[0].text)), nb_bikes = ele.xpath("nbBikes")[0].text, nb_empty_docks = float(ele.xpath("nbEmptyDocks")[0].text), updated_at = timezone.now(), last_comm_with_server = lastUpdate)
                    s.save()
                else:
                    station = StationDataNow.objects.get(station = Station.objects.get(station_id = int(ele.xpath("id")[0].text)))
                    station.nb_bikes = int(ele.xpath("nbBikes")[0].text)
                    station.nb_empty_docks = int(ele.xpath("nbEmptyDocks")[0].text)
                    station.updated_at = timezone.now()
                    station.last_comm_with_server = lastUpdate

        self.stdout.write('Successfully updated station data')
                    
        # for poll_id in options['poll_id']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write('Successfully closed poll "%s"' % poll_id)
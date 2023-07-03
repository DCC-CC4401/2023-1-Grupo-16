from app_inicial.models import Location

def create_initial_locations():
        if Location.objects.filter(name='Club Hípico').exists()!=True:
                Location.objects.create(
                        name='Club Hípico', 
                        address='Club Hípico 1001',
                        city='Santiago',
                        country='Chile',
                ).save()
        if Location.objects.filter(name='Teatro Cariola').exists()!=True:
                Location.objects.create(
                        name='Teatro Cariola',
                        address='San Diego 246',
                        city='Santiago',
                        country='Chile',
                ).save()
        if Location.objects.filter(name='Teatro Caupolicán').exists()!=True:
                Location.objects.create(
                        name='Teatro Caupolicán',
                        address='San Diego 850',
                        city='Santiago',
                        country='Chile',
                ).save()
        if Location.objects.filter(name='Movistar Arena').exists()!=True:
                Location.objects.create(
                        name='Movistar Arena',
                        address='Tupper 250',
                        city='Santiago',
                        country='Chile',
                ).save()
        if Location.objects.filter(name='Estadio Nacional').exists()!=True:
                Location.objects.create(
                        name='Estadio Nacional',
                        address='Av. Grecia 2001',
                        city='Santiago',
                        country='Chile',
                ).save()
        if Location.objects.filter(name='Estadio Monumental').exists()!=True:
                Location.objects.create(
                        name='Estadio Monumental',
                        address='Av. Marathon 5300',
                        city='Santiago',
                        country='Chile',
                ).save()
        if Location.objects.filter(name='Estadio Bicentenario de la Florida').exists()!=True:
                Location.objects.create(
                        name='Estadio Bicentenario de la Florida',
                        address='Av. Vicuña Mackenna 1175',
                        city='Santiago',
                        country='Chile',
                ).save()
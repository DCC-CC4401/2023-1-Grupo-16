from app_inicial.models import Location

initial_locations = {
        'Club Hípico': {
                'address': 'Club Hípico 1001',
                'city': 'Santiago',
                'country': 'Chile',
        },
        'Teatro Cariola': {
                'address': 'San Diego 246',
                'city': 'Santiago',
                'country': 'Chile',
        },
        'Teatro Caupolicán': {
                'address': 'San Diego 850',
                'city': 'Santiago',
                'country': 'Chile',
        },
        'Movistar Arena': {
                'address': 'Tupper 250',
                'city': 'Santiago',
                'country': 'Chile',
        },
        'Estadio Nacional': {
                'address': 'Av. Grecia 2001',
                'city': 'Santiago',
                'country': 'Chile',
        },
        'Estadio Monumental': {
                'address': 'Av. Marathon 5300',
                'city': 'Santiago',
                'country': 'Chile',
        },
        'Estadio Bicentenario de la Florida': {
                'address': 'Av. Vicuña Mackenna 1175',
                'city': 'Santiago',
                'country': 'Chile',
        },
        'Casa CEI': {
                'address': 'Tupper 2140',
                'city': 'Santiago',
                'country': 'Chile',
        },
}

def create_initial_locations():
        for location in initial_locations:
                if Location.objects.filter(name=location).exists()!=True:
                        Location.objects.create(
                                name=location,
                                address=initial_locations[location]['address'],
                                city=initial_locations[location]['city'],
                                country=initial_locations[location]['country'],
                        ).save()
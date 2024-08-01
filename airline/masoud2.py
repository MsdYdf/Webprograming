from flights.models import Flight

flight=Flight.objects.all()
SYMBOLS = [k for k in locals().keys() if not k.startswith('_')]

if __name__ == '__main__':
    print(flight.SYMBOLS)

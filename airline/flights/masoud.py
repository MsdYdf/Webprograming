from .models import Flight, Passenger

flight=Flight.objects.get(pk=1)
passengers = flight.passengers.all()
non_passengers = Passenger.objects.exclude(flights=flight).all()
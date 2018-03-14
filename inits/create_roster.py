# This will create a user
# run from resQmia ROOT
# python manage.py shell
# execfile('./inits/create_roster.py')

from apps.baseball_app.models import Player

Home = [[1, Scott, Podsednik], [2, Tadahito, Iguchi],[3, Carl, Everett], [4, Paul, Konerko], [5, Jermaine, Dye], [6, Aaron, Rowand], [7, AJ, Pierzynski], [8, Joe, Crede], [9, Juan, Uribe]]

Away = [[1, Dexter, Fowler], [2, Kris, Bryant], [3, Anthony, Rizzo], [4, Ben, Zobrist], [5, Addison, Russell], [6, Jason, Heyward], [7, Jorge, Soler], [8, David, Ross], [9, Kyle, Schwarber]]

for x in Home:
    team = Home
    order = x[0]
    first_name = x[1]
    last_name = x[2]
    
    Player.objects.create(team=team, order=order, first_name=first_name, last_name=last_name)

for y in Away:
    team = Away
    order = y[0]
    first_name = y[1]
    last_name = y[2]
    
    Player.objects.create(team=team, order=order, first_name=first_name, last_name=last_name)

# This will create the roster
# run from resQmia ROOT
# python manage.py shell
# execfile('./inits/create_roster.py')

from apps.baseball_app.models import Player

Home = [[1, "Scott", "Podsednik"], [2, "Tadahito", "Iguchi"],[3, "Carl", "Everett"], [4, "Paul", "Konerko"], [5, "Jermaine", "Dye"], [6, "Aaron", "Rowand"], [7, "AJ", "Pierzynski"], [8, "Joe", "Crede"], [9, "Juan", "Uribe"]]

Away = [[10, "Dexter", "Fowler"], [11, "Kris", "Bryant"], [12, "Anthony", "Rizzo"], [13, "Ben", "Zobrist"], [14, "Addison", "Russell"], [15, "Jason", "Heyward"], [16, "Jorge", "Soler"], [17, "David", "Ross"], [18, "Kyle", "Schwarber"]]

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

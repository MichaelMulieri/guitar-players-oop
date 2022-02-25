class Manager:
    def __init__(self, name):
        self.name = name
        self.player_name = None

    def pick_player(self, player):
        self.player_name = player

    def dock_pay(self, money):
        self.player_name.money -= money


class guitar_player:

    all_players = []

    def __init__(self, player_name, band_name, make, model, color, pickups, amp, amp_volume, money, bass_player = None):
        self.player_name = player_name
        self.band_name = band_name
        self.make = make
        self.model = model
        self.color = color
        self.pickups = pickups
        self.amp = amp
        self.amp_volume = amp_volume
        self.bass_player = bass_player
        self.money = money 
        guitar_player.all_players.append(self)

    def change_amp_volume(self, amp_volume):
        self.amp_volume = amp_volume 
        return self

    def change_guitar(self, make, model, color, pickups):
        self.make = make
        self.model = model
        self.color = color
        self.pickups = pickups
        return self

    def change_player_name(self, player_name):
        self.player_name = player_name
        return self

    def change_band(self, band_name):
        self.band_name = band_name
        return self

    def change_bass_player(self, bass_player):
        self.bass_player = bass_player
        return self

    def print_player(self):
        return(f'''Name: {self.player_name} 
        Band: {self.band_name}
        Guitar Brand: {self.make} 
        Guitar Model: {self.model}
        Guitar Color: {self.color}
        Pickup Type: {self.pickups} 
        Amp Brand: {self.amp} 
        Amp Volume: {self.amp_volume} 
        Cash: {self.money}
        Bass Player: {self.bass_player}''')
        

    @classmethod
    def print_all_players(cls):
        for player in cls.all_players:
            player.print_player()



tim = guitar_player("Tim Armstrong", "Rancid", "Gretsch", "Country Club", "Black", "Filtertron", "Mesa Boogie", 8, 5000, "Matt Freeman")
ivy = guitar_player("Poison Ivy", "The Cramps", "Gretsch", "6120", "Orange", "Filtertron", "Fender", 10, 3000)
johnny = guitar_player("Johnny Marr", "The Smiths", "Fender", "Jazz Master", "White", "JM", "Roland", 7, 7000, "Andy Rourke")
mike = guitar_player("Mike Ness", "Social Distortion", "Gibson", "Les Paul", "Gold Top", "P-90", "Fender", 9, 5500, "John Maurer")
john = guitar_player("Speedo", "Rocket From The Crypt", "Gibson", "Les Paul", "Sparkle", "Humbucker", "Marshall", 10, 6000, "Petey X")
        
"""johnny.change_band("The Cribs").change_bass_player("Gary Jarman").change_guitar("Rickenbacker", "330", "Jet Glo", "Single Colil").change_amp_volume(9)
johnny.print_player()

john.change_band("Plosivs").change_bass_player("Jordan Clark").change_player_name("John Reis").change_guitar("Fender", "Telecaster", "Blonde", "Single Coil")
john.print_player()"""

brian = Manager("Brian Epstein")
malcolm = Manager("Malcolm McLaren")

brian.pick_player(tim)
malcolm.pick_player(ivy)

print(tim.print_player())
#print(ivy.print_player())
print(brian.dock_pay(800))
print(tim.print_player())


#guitar_player.print_all_players()











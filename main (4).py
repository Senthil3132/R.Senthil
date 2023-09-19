class player:
  def play (self):
    print("The Player is playing Cricket")
class batsman (player):
  def play(self):
    print ("The Batsman is Batting. ")
class bowler(player):
  def play(self):
    print (" The Bowler is Bowling")
Batsman=batsman() 
Bowler=bowler()


Batsman.play() 
Bowler.play ()
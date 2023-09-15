class Player:

  def play(self):
    print("the player is playing cricket.")


class Batsman(Player):

  def play(self):
    print("the batsman  is bating.")


class Bowler(Player):

  def play(self):
    print("the bowler is bowling.")


batsman = Batsman()
bowler = Bowler()
player = Player()
player.play()
batsman.play()
bowler.play()

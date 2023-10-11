class Game:
    def __init__(self, title):
        self.title = title

        self._results = []
        self._players = []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) == str and len(title) > 0 and not hasattr(self, "title"):
            self._title = title
        # else:
        #     raise Exception("Title must be a string containing at least one character!")

    def results(self):
        return self._results

    def players(self):
        return list(set(self._players))

    def average_score(self, player):
        return sum([result.score for result in player._results]) / len(player._results)

class Player:
    def __init__(self, username):
        self.username = username

        self._results = []
        self._games_played = []

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if type(username) == str and 2 <= len(username) <= 16:
            self._username = username
        # else:
            # raise Exception("Username must be a string containing between 2 and 16 characters!")

    def results(self):
        return self._results

    def games_played(self):
        return list(set(self._games_played))

    def played_game(self, game):
        if game in self.games_played():
            return True
        else:
            return False

    def num_times_played(self, game):
        times_played = 0
        for item in self._games_played:
            if item == game:
                times_played += 1
        return times_played

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        self.player._results.append(self)
        self.player._games_played.append(self.game)

        self.game._results.append(self)   
        self.game._players.append(self.player)

        Result.all.append(self)

    # Player property
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        # else:
        #     raise Exception

    # Game property
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        # else:
        #     raise Exception

    # Score 
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if type(score) == int and 1 <= score <= 5000 and not hasattr(self, "score"):
            self._score = score
        # else:
        #     raise Exception("Score must be an integer between 1 and 5,000!")
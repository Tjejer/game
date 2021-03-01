"""Class for highscore."""

# import player


class Highscore():
    """Createing class."""

    file_name = None

    def __init__(self, file_name):
        """When highscore is created."""
        self.file_name = file_name

    def log_score(self, score, player_id):
        """Score logs."""
        high_file = open(self.file_name, 'a')
        high_file.write(str(player_id) + ":" + str(score) + '\n')
        high_file.close()

    def get_scores(self):
        """Gettin scores."""
        high_file = open(self.file_name, 'r')
        lines = high_file.read().split('\n')
        high_file.close()
        return lines

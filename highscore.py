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
        high_file.write(str(score) + ":" + str(player_id) + '\n')
        high_file.close()

    def get_scores(self):
        """Gettin scores."""
        high_file = open(self.file_name, 'r')
        lines = high_file.read().split('\n')
        lines = list(filter(str.strip, lines))
        high_file.close()
        return lines

    def sort_scores(self, lines):
        """Sorting the highscores. Highest on top."""
        # lambda found at: https://stackoverflow.com/questions/
        # 21431052/sort-list-of-strings-by-a-part-of-the-string
        lines.sort(key=lambda x: x.split(':')[0])
        high_file = open(self.file_name, 'w')
        for line in lines:
            high_file.write(str(line) + '\n')
        high_file.close()
        return lines

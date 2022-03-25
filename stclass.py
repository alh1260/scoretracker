class ScoreTracker:
    """
    A class to represent a score manager.
    """
    def __init__(self, max_score, members):
        """
        CONSTRUCTOR: ScoreTracker(int, list<str>)
        Creates a new ScoreTracker instance with a specified maximum score
        and names of members.

        parameters:
        <int> max_score
            The maximum score that individual scores in this tracker must
            add up to.
        <list<str>> members
            A list of all the member names to track. These will be used as
            keys
        """
        # INSTANCE VARIABLES
        # the maximum score
        self._max_score = max_score
        # the map of individual members' scores
        # type: dict<str, float>
        self._score_map = {}
        # for (String name : members)
        for name in members:
            self._score_map[name] = self._max_score / len(members)

    def showScore(self):
        for name in self._score_map.keys():
            print("{0}:{1}".format(name, self._score_map[name]))

    def updateScore(self, member, new_score):
        """
        Updates the scores

        parameters:
        <str> member
             the name of the specified member
        <int> new_score
             the score value that replaces the previous value
        """
        self._score_map[member] = new_score
        # now to recalculate
        members = self._score_map.keys()
        # first sum up the current scores
        score_sum = 0
        for name in members:
            score_sum += self._score_map[name]
        difference = score_sum - self._max_score
        # then get the excess to subtract from the other scores
        excess = difference / (len(members) - 1)
        for name in members:
            if name != member:
                self._score_map[name] -= excess

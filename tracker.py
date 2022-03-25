#!/usr/bin/env python3

# argv format:
# tracker.py <member1> <member2> [<member3> [...]]

import sys
from stclass import ScoreTracker

def mainloop():
    member_list = sys.argv[1:]
    if len(member_list) == 0:
        print("usage: tracker.py <member1> <member2> [<member3> [...]]")
        exit(1)
    max_score = input("Enter a maximum score: ")
    score_tracker = ScoreTracker(int(max_score), member_list)
    print("scores:")
    score_tracker.showScore()
    while True:
        command = input("score tracker> ")
        if command == "quit":
            print("Goodbye.")
            break
        elif command[:7] == "update ":
            # cmd fmt: update <member> <value>
            param_string = command[7:]
            # params = [<member>, <value>]
            params = param_string.split()
            score_tracker.updateScore(params[0], float(params[1]))
            print("scores:")
            score_tracker.showScore()
            continue
        else:
            print("Unknown command")
            continue
    exit

if __name__ == '__main__':
    mainloop()

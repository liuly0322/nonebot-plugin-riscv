def word_diff(start, goal):
    """A diff function that computes the edit distance from START to GOAL."""
    memo = dict()

    def recur(start, goal):
        if start == '' or goal == '':  # base case
            return max(len(start), len(goal))

        else:
            if memo.get((start, goal)):
                return memo.get((start, goal))
            skip = 1 if start[0] != goal[0] else 0
            add_diff = recur(start, goal[1:]) + 1
            remove_diff = recur(start[1:], goal) + 1
            substitute_diff = recur(start[1:], goal[1:]) + skip
            memo[(start, goal)] = min(add_diff, remove_diff, substitute_diff)
            return memo[(start, goal)]

    return recur(start, goal)

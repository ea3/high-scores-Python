def latest(scores):
    latest_score = scores.pop()
    return latest_score


def personal_best(scores):
    best_score = max(scores)
    return best_score


def personal_top_three(scores):
    sorted_scores = sorted(scores)[::-1]
    # max_scores = []
    if len(sorted_scores) == 1:
        first_score = [sorted_scores[0]]
        return first_score
    elif len(sorted_scores) == 2:
        first_two_scores = [sorted_scores[0], sorted_scores[1]]
        return first_two_scores
    else:
        first_three_scores = [sorted_scores[0], sorted_scores[1], sorted_scores[2]]
        return first_three_scores


# personal_top_three([100, 10, 50, 40, 30, 20])

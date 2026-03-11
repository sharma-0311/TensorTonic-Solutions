def random_forest_vote(predictions):
    """
    Compute majority vote for each sample using dictionary counting.
    Tie breaks by smallest class label.
    """
    n_trees = len(predictions)
    n_samples = len(predictions[0])

    result = []

    for i in range(n_samples):
        freq = {}

        # count votes from each tree
        for tree in range(n_trees):
            label = predictions[tree][i]

            if label in freq:
                freq[label] += 1
            else:
                freq[label] = 1

        # max count
        max_count = max(freq.values())

        # tie break: smallest label among max count labels
        winners = [k for k, v in freq.items() if v == max_count]

        result.append(min(winners))

    return result
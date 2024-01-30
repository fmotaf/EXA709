def sum_(dataset: any, keys: tuple, check: tuple = None):
    sets = []
    for key in keys:
        sets.append(dataset[key])
    total_items = 0
    prob_and = {}
    percentage_and = {}
    prob_count = {}
    percentage_count = {}
    for item in zip(*tuple(sets)):
        total_items += 1

        if check:
            for item_check in check:
                key_prob = " && ".join(item_check)
                add = True
                for i, c in enumerate(item_check):
                    if item[i] != c:
                        add = False
                if add:
                    if key_prob not in prob_and:
                        prob_and[key_prob] = 1
                    else:
                        prob_and[key_prob] += 1

        for i, key in enumerate(keys):
            key_prob = "%s -> %s" % (key, item[i])
            if key_prob not in prob_count:
                prob_count[key_prob] = 1
            else:
                prob_count[key_prob] += 1

    for key in prob_and.keys():
        percentage_and[key] = float("%.2f" % ((prob_and[key] / total_items) * 100))

    for key in prob_count.keys():
        percentage_count[key] = float("%.2f" % ((prob_count[key] / total_items) * 100))

    return {
        "and": prob_and,
        "raw": prob_count,
        "probability_and": percentage_and,
        "probability_raw": percentage_count,
        "total": total_items,
    }


def calc_(a: int, set: int):
    return float("%.2f" % a / set)

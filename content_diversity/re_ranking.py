def mmr(recommended_items, lambda_param=0.5):
    re_ranked = []
    while recommended_items:
        item = recommended_items.pop(0)
        if not re_ranked:
            re_ranked.append(item)
        else:
            similarity = max([similarity_measure(item, re_ranked_item) for re_ranked_item in re_ranked])
            if similarity < lambda_param:
                re_ranked.append(item)
    return re_ranked

def similarity_measure(item1, item2):
    return abs(item1 - item2)

recommended_items = [1, 2, 3, 4, 5]
re_ranked_items = mmr(recommended_items)
print(re_ranked_items)

import random

from config import MESSAGE_LEN, VARIANT_LEN, VARIANT_NUM


def filtered(s: str):
    res = ""
    for c in s:
        if c.isalnum():
            res += c
    return res


def parser(query: str):
    variants = query.split(' ')
    result = []
    for variant in variants:
        if len(variant) > VARIANT_LEN:  # exception processed
            return [], "Error: length limit exceeded"

        variant_filtered = filtered(variant)
        if len(variant_filtered) > 0:
            result.append(variant_filtered)

    return result, "ok"


def get_message(query: str, show_variants=True):
    variants, status = parser(query)
    if status.startswith("Error"):
        return status
    if len(variants) == 0:
        return "Error: no valid variants"

    choice = random.choice(variants)
    probability = f"{1 / len(variants) * 100:.2f}%"
    message = f"\n<b>{choice}</b> \n\nProbability: {probability}"
    if show_variants:
        message += "\n\nVariants:\n"
        for var_id in range(len(variants)):
            tail = f"{var_id + 1}. {variants[var_id]}"
            if len(message) + len(tail) > MESSAGE_LEN or var_id == VARIANT_NUM:
                message += "..."
                break
            else:
                message += tail + '\n'

    return message

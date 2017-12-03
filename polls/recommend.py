from autocorrect import spell

def not_found(incorrect):
    new_string = spell(incorrect)
    return new_string

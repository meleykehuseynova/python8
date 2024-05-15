def samitleri_al(cumle):
    samitler = set()
    for harf in cumle:
        if harf.isalpha() and harf.lower() not in "aeiou":
            samitler.add(harf.lower())
    return samitler
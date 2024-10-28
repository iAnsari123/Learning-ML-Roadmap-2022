def chrismas_wish(billengual_dictionary, language):
    for word in language.split():
        print(billengual_dictionary[word], end=" ")


chrismas_wish(
    {
        "merry": "god",
        "christmas": "jul",
        "and": "och",
        "happy": "gott",
        "new": "nytt",
        "year": "ar",
    },
    "merry christmas and happy new year",
)

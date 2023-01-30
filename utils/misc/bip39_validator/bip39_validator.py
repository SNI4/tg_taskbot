
async def async_validate_bip39(phrase: str) -> bool:
    wordlist = open('utils/misc/bip39_validator/wordlist.txt')
    words = wordlist.read().splitlines()
    phrase_words = phrase.split()
    if ((len(phrase_words) % 3) != 0) or (len(phrase_words) > 24):
        print("Падает в количестве")
        return False

    for word in phrase_words:
        if word in words:
            pass
        else:
            print("Падает в словах")
            return False
    return True

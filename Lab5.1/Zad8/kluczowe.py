import keyword

keywords = ["for", "print", "break", "done", "bad"]
results = {word: word in keyword.kwlist for word in keywords}
results
def ft_filter(string: str, number: int) -> int:
    """
    Return an iterator yielding those items of iterable
    for which function(item)
    is true. If function is None, return the items that are true.
    """
    words = string.split()
    filtered_words = [w for w in words if len(w) >= number]
    print(f"{filtered_words}")

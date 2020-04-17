def sort_by_name(function_arg):
    def add_words(*args, **kwargs):
        original_string = function_arg(*args, **kwargs)
        return f"{original_string} ORDER BY last_name ASC, first_name ASC"
    return add_words

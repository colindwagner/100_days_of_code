
#functions with outputs

def my_function():
    result = 2 * 3
    return result

print(my_function())


def format_name(fname, lname):
    formatted_fname = fname.title()
    formatted_lname = lname.title()

    return f"{formatted_fname} {formatted_lname}"


print(format_name("colIn", "waGner"))
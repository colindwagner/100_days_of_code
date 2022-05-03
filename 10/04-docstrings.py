

#docstrings have the ability to comment and document code and output it to an ide


def format_name(fname, lname):
    """Take a first nand last name and format it
    to return the title case version of the name"""

    if fname == "" or lname == "":
        return "You didnt put in names"

    formatted_fname = fname.title()
    formatted_lname = lname.title()

    return f"{formatted_fname} {formatted_lname}"


print(format_name("colIn", "waGner"))

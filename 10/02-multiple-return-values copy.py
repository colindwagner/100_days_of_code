
#multiple return values

def format_name(fname, lname):
    if fname == "" or lname == "":
        return "You didnt put in names"

    formatted_fname = fname.title()
    formatted_lname = lname.title()

    return f"{formatted_fname} {formatted_lname}"


print(format_name("colIn", "waGner"))
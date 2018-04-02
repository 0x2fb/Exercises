def titleize(s):
    return " ".join([i[0].title() + i[1:] for i in s.split()])


print(titleize('this is awesome'))  # "This Is Awesome"
print(titleize('oNLy cAPITALIZe fIRSt'))  # "ONLy CAPITALIZe FIRSt"

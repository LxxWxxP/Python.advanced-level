
def format_name(s):
    return s[:1].upper()+s[1:].lower()

print map(format_name, ['adam', 'LISA', 'barT'])

def format_name(s):
    return s.capitalize()

print map(format_name, ['adam', 'LISA', 'barT'])

def format_name(s):
    return str.capitalize(s)

print map(format_name, ['adam', 'LISA', 'barT'])
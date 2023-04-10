import re
def read_template(arg):
    if arg not in ["assets/dark_and_stormy_night_template.txt", "assets/cliGame.txt"]:
        raise FileNotFoundError("Error: Invalid file path.")
    with open(arg) as file:
        content = file.read()
    return content

def parse_template(tex):
    content=tex
    pattern=r"{(\w+)}"
    matches = re.sub(pattern,"{}", content)
    result = re.findall(pattern, content)
    buple = ()
    for item in result:    
     y = list(buple)
     y.append( item)
     buple = tuple(y)

    return matches,buple
def merge(tex,tuple):
    y = list(tuple)
    txt = tex.format(*y)
    return txt


if __name__ == "__main__":
    print("welcom to our funny game, play by entering what you are asked ;)")
    
    template = read_template("assets/cliGame.txt")
    stripped_template, parts = parse_template(template)

    user_inputs = []
    for part in parts:
        user_inputs.append(input(f"Enter a {part}: "))
    x = ()
    for item in user_inputs:    
     y = list(x)
     y.append( item)
     x = tuple(y)
    text = merge(stripped_template, x)
    print(text)
    with open("madlib_cli/assets/text.txt", "w") as file:
        opened_file =file.write(text)
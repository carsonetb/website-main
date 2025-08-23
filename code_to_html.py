import re

filepath = "codefile"
output = "codehtml"

in_file = open(filepath, "r")
out_file = open(output, "w")

valid_numberparts = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

def format_text_color(keywords, color, italics=False):
    temp = text
    for keyword in keywords:
        temp = temp.replace(keyword, ("<i>" if italics else "") + "<span style='color:" + color + ";'>" + keyword + "</span>" + ("</i>" if italics else ""))
    return temp

def format_inside(start_keyword, end_keyword, color):
    temp = text
    indices = [match.start() for match in re.finditer(start_keyword, temp)]
    for i in range(len(indices)):
        start = indices[i]
        end = temp.find(end_keyword, start)
        temp = temp[:start + len(start_keyword)] + "<span style='color:" + color + ";'>" + temp[start + len(start_keyword):end] + "</span>" + temp[end:]
        indices = [match.start() for match in re.finditer(start_keyword, temp)]
    return temp

def format_numbers(before):
    temp = text
    indices = [i for i, val in enumerate(temp) if val == before]
    ind_ind = -1
    for potentnum in temp.split(before):
        ind_ind += 1
        i = 0
        if ind_ind >= len(indices):
            break
        if potentnum == "":
            continue
        while True:
            if potentnum[-i - 1] in valid_numberparts:
                i += 1
                continue
            break
        if i == 0:
            continue
        temp = temp[:indices[ind_ind] - i] + "<span style='color: #FF813F'>" + temp[indices[ind_ind] - i:indices[ind_ind]] + "</span>" + temp[indices[ind_ind]:]
        indices = [i for i, val in enumerate(temp) if val == before]
    return temp

def format_quotes(color):
    temp = text
    inside = False
    i = -1
    while i + 1 < len(temp):
        i += 1
        if temp[i] == "\"":
            if not inside:
                temp = temp[:i] + "\"<span style='color:" + color + ";'>" + temp[i + 1:]
                i += 30
            if inside:
                temp = temp[:i] + "</span>" + temp[i:]
                i += 7
            inside = not inside
    return temp

prefix = "<!-- Generated from a seperate code file for HTML -->\n<code>\n    "
text = in_file.read()
text = text.replace("    ", "&nbsp&nbsp ")
text = text.replace("<", "&lt")
text = text.replace(">", "&gt")
text = format_numbers(",")
text = format_numbers(")")
text = format_numbers(";")
text = format_inside("#include &lt", "&gt", "#9ECE6A")
text = format_inside(" namespace ", ";", "#0FB4B5")
text = format_quotes("#9EB74C")
text = text.replace("\n", "<br>")
text = format_text_color(["\""], "#77D0F8")
text = format_text_color(["include ", " namespace ", "int ", "do ", "while ", "char", "if ", "else ", "float", "&&", "||", "==", "!=", "&lt=", "&gt=", "void ", "bool "], "#B692B9")
text = format_text_color(["return ", "static ", "const "], "#B692B9", italics=True)
text = format_text_color(["&lt", "&gt", "using", "*", " / ", "+", "-"], "#77D0F8")
text = format_text_color(["(", ")"], "#56B3D2")
text = format_inside("//", "<br>", "#707070")
text = format_text_color(["//"], "#707070")
text = prefix + text
text += "\n</code>"

out_file.write(text)
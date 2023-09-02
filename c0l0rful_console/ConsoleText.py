

def UniqueColorConverter(Text, Color):
    ColorSelected = None
    if IsValidColor(Color):
        if Color.startswith("#"):
            R = int(Color[1:3], 16)
            G = int(Color[3:5], 16)
            B = int(Color[5:7], 16)
            ColorSelected = f"\033[38;2;{R},{G};{B}m"
        if Color == "red":
            ColorSelected = "\033[38;2;255;0;0m"
        elif Color == "blurple":
            ColorSelected = "\033[38;2;45;95;247m"
        ColoredText = ColorSelected + Text
        return ColoredText
    else:
        return Text

def IsValidColor(Color):
    SupportedColors = [
        "red",
        "blurple"
    ]
    if Color in SupportedColors or (Color.startswith("#") and len(Color) ==7):
        return True
    else:
        return False
import os

def vel(height, skin):
    if skin == "circ0":
        return 20
    if skin == "line0":
        return 15
    if skin == "round0":
        return 15
    
    else:
        if height >= 70:
            return 20
        if height < 70:
            return 15
        
def skins():
    note_skins = []
    back_skins = []
    for file in os.listdir("images"):
        if "0" in file or "1" in file:
            note_skins.append(file[:-4])
        else:
            back_skins.append(file[:-4])
    return [note_skins, back_skins]

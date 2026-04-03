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
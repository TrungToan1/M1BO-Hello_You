verzekering_per_maand =  23
benzine_kosten_per_liter =  1.54
liter_per_kilometer = 0.2


def bereken_maandkosten():
    km_per_maand = if int(input("Hoeveel kilometer: ")) / liter_per_kilometer * benzine_kosten_per_liter + verzekering_per_maand
    
    print(km_per_maand)

bereken_maandkosten()
def build_facility_report(arboretum):
    for river in arboretum.rivers:
        print(f'{river.name} - {river.id}')
        print(
            f"This place has {len(river.animals)} animals and {len(river.plants)} plants in it")

    for swamp in arboretum.swamps:
        print(f'{swamp.name} - {swamp.id}]')

    input("\n\nPress any key to continue...")

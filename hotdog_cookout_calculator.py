from math import ceil

hotdogs_per_pack = 10
buns_per_pack = 8

attendees = int(input("\nEnter the number of people attending the cookout: "))
hotdogs_per_person = int(input("Enter the number of hot dogs each person will"\
                               " be given: "))
hotdogs_total = hotdogs_per_person * attendees

min_hotdog_packs = ceil(hotdogs_total / hotdogs_per_pack)
min_buns_packs = ceil(hotdogs_total / buns_per_pack)
hotdogs__leftover = (hotdogs_per_pack * min_hotdog_packs) - hotdogs_total
buns_leftover = (buns_per_pack * min_buns_packs) - hotdogs_total

print("\nMinimum number of packages of hot dogs required:", min_hotdog_packs)
print("Minimum number of packages of hot dog buns required:", min_buns_packs)
print("\nNumber of hot dogs that will be left over:", hotdogs__leftover)
print("Number of hot dog buns that will be left over:", buns_leftover)
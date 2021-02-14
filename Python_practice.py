counties = ["Arapahoe", "Denver", "Jeferson"]
if "Arapahoe" in counties and "El Paso" not in counties:
     print("Only Arapahoe is in the list of counties.")
else:
   print("Only Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for i in range(len(counties)):
     print(counties[i])
         

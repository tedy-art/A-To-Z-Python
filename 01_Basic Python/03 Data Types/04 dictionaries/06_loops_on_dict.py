# for loop `keys`
thisdict =	{
  "brand": "HP",
  "model": "pavilion 360",
  "year": 2016
}
print("Keys")
for i in thisdict:
    print(i)

print()
# for loop on `values`
thisdict =	{
  "brand": "HP",
  "model": "pavilion 360",
  "year": 2016
}
print("values")
for i in thisdict:
    print(thisdict[i])

print()
thisdict =	{
  "brand": "HP",
  "model": "pavilion 360",
  "year": 2016
}
for x in thisdict.values():
  print(x)
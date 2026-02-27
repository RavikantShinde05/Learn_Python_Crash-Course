# FOR-ELSE LOOP:

successfull = True

for i in range(3):
    print("tried")
    if successfull:
        print("done")
    break  # If it is tried then the loop will break or else tried is printed 3 times
else:
    print("not Done")

unsuccessfull = True
for i in range(3):
    print("tried")
    if unsuccessfull:
        print("not done")
    break
else:
    print("Done")

from datetime import datetime

print("Aao MAHARATHI!!!")

date_input = input("Enter a date (DD-MM-YYYY): ")
date_time = datetime.strptime(date_input, "%d-%m-%Y")
date = date_time.date()

filename = f"{date}.txt"


with open(filename, "a+") as f:
    f.seek(0)                     
    content = f.readlines()


if not content:
    with open(filename, "w") as f:
        f.write("#TO-DO LIST\n")
    content = ["#TO-DO LIST\n"]


last_index = 0
for line in content:
    if line.strip() and line[0].isdigit():
        last_index = int(line.split(".")[0])


while True:
    inp = input("What do you want to do (Y=add, V=view, N=exit)? ").upper()

    if inp == "Y":
        last_index += 1
        entry = input(f"Entry {last_index}: ")
        with open(filename, "a") as f:
            f.write(f"{last_index}. {entry}\n")
        print(f"Entry {last_index} added!")

    elif inp == "V":
        with open(filename, "r") as f:
            print(f.read())

    elif inp == "N":
        print("Ok bye bhai")
        break

    else:
        print("netra kholo maharathi !")

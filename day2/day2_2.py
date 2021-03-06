def main():
    with open('day2_input.txt') as f:
        lines = f.readlines()
    f.close()
    
    posx = 0
    posy = 0
    aim = 0

    for line in lines:
        line = line.replace("\n","").split(" ")
        if line[0] == "up":
            aim = aim - int(line[1])
        elif line[0] == "down":
            aim = aim + int(line[1])
        elif line[0] == "forward":
            posx = posx + int(line[1])
            posy = posy + (aim * int(line[1]))
        else:
            print("ERROR")

    print("Vertical Position: " + str(posy))
    print("Horizontal Position: " + str(posx))
    print("Solution: " + str(posx * posy))

main()
# Answer is 1759818555
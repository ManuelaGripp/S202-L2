from zoologicoCLI import ZoologicoCLI

flag = True
CLI = ZoologicoCLI()

while flag:
    result = CLI.menu()

    match result:
        case '1':
            CLI.createAnimal()
        case '2':
            CLI.readAnimal()
        case '3':
            CLI.updateAnimal()
        case '4':
            CLI.deleteAnimal()
        case '5':
            flag = False
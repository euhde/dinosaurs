dinosaurs = [['Tyrannosaurus', 16000, 'carnivore', 'Late Cretaceous'],
            ['Ankylosaurus', 10000, 'herbivore', 'Late Cretaceous'],
            ['Stegosaurus', 6000, 'herbivore', 'Late Jurassic'],
            ['Deinonychuys', 175, 'carnivore', 'Early Cretaceous']]

output = '{0:20} {1:15} {2:15} {3:20}'

print (output.format('Name', 'Weight (lbs)', 'Diet', 'Time'))
print ('-' * 70)

for dinosaur in dinosaurs:
    name, weight, diet, time = dinosaur
    print (output.format (name, str(weight), diet, time))
    

def table_print (headers, data, width):

    output = '{:{}} {:{}}'

    print (output.format (headers[0], width, headers[1], width))

    print ('-' * (width + 1) * 2)

    for item in data:
        print (output.format(item[0], width, item[1], width))
        
    print ()


labels = ['Nest', 'Eggs']
nests = []

longest = 0

while True:
    
    dinoName = input ('\nPlease enter the dinosaur\'s name: ')

    while True:

        eggCount = input ('Please enter how many eggs were found: ')

        try:
            val = int(eggCount)
            break
        except ValueError:
            print ('Please enter an integer\n')
            continue
    
    nests.append ((dinoName, eggCount))

    if len(dinoName) > longest:
        longest = len(dinoName)

    if len(eggCount) > longest:
        longest = len(eggCount)



    print ('Current fossilized dinosaur egg count:\n')
    table_print (labels, nests, longest + 2)

    continueVal = input ('Continue entering dinosaurs? ')
    if continueVal.lower() == 'no':
        break
    if continueVal.lower() == 'yes':
        continue

        

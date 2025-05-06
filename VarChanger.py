from pathlib import Path
print("Script creato per tamponare gli shape nelle pagine dei progetti Winpage.\n\n")
fileToRead=input("Trascina il file da convertire all'interno della finestra:\n")
groupToChange=input("Inserisci il riferimento delle shape a cui cambiare il range di X: ( Per esempio FS1_Hdl6_B2 o D1_Hdl2_R27) \n")
varToChange=input("Vuoi cambiare la X o la Y? \n")
howMuch=int(input("Di quanto vanno cambiati i limiti massimi e minimi? (Esempio -6000 o +100)\n"))

lineToBeChecked='<AnimationLink Type="RectangleFromVariable" LinkedProperty="Rectangle" VariableX="'+groupToChange
allLinesToBeWritten=[]

if varToChange == "X" or varToChange == "x" :
    maxLimit=224000+howMuch
    stringToBeReplaced='VariableRangeLoc'+varToChange+'="0, 224000"'
else:
    maxLimit=28000+howMuch
    stringToBeReplaced='VariableRangeLoc'+varToChange+'="0, 28000"'

minLimit=0+howMuch
fileToRead=fileToRead.removeprefix("& '")
fileToRead=fileToRead.removeprefix('"')
fileToRead=fileToRead.removesuffix("'")
fileToRead=fileToRead.removesuffix('"')
lastSegment=fileToRead.rindex('.')
stringToReplace='VariableRangeLoc'+varToChange+'="'+str(minLimit)+', '+str(maxLimit)+'"'

with open(fileToRead,"r") as file:
    allLines=file.readlines()
    for line in allLines:
        if lineToBeChecked in line:
            modifiedLine=line.replace(stringToBeReplaced,stringToReplace)
            allLinesToBeWritten.append(modifiedLine)
        else:
            allLinesToBeWritten.append(line)

pathToWrite=fileToRead[:lastSegment]+'_modified.wppage'
filePath=Path(pathToWrite)
if filePath.exists():
    with open(pathToWrite,'w') as file:
        file.writelines(allLinesToBeWritten)
else:
    with open(pathToWrite,'x') as file:
        file.writelines(allLinesToBeWritten)

input("\nTrovi il file modificato al percorso:  "+pathToWrite+"\nPremi Invio per chiudere...")
while True :
    Output = input("Enter some text: ")
    user_input=(Output)
    if 'a' in Output or 'A' in Output :
        Output = Output.replace('a', '*')
        Output = Output.replace('A', '*')
    if 'i' in Output or'I' in Output  :
        Output = Output.replace('i', '*')
        Output = Output.replace('I', '*')
    if 'e' in Output or'E' in Output  :
        Output = Output.replace('e', '*')
        Output = Output.replace('E', '*')
    if 'u' in Output or'U' in Output :
        Output = Output.replace('u', '*')
        Output = Output.replace('U', '*')
    if 'o' in Output or 'O' in Output :
        Output = Output.replace('o', '*')
        Output = Output.replace('O', '*')
    print(Output)
    print(user_input)

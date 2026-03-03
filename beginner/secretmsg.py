string = input("Enter a message to be encrypted: ").lower() 

alpha_dict = {'a':'z', 'b':'y', 'c':'x', 'd':'w', 'e':'v', 'f':'u', 'g':'t', 'h':'s', 'i':'r', 'j':'q', 'k':'p', 'l':'o', 'm':'n', 'n':'m', 'o':'l', 'p':'k', 'q':'j', 'r':'i', 's':'h', 't':'g', 'u':'f', 'v':'e', 'w':'d', 'x':'c', 'y':'b', 'z':'a'}
s = ""
for i in string:
    if i in alpha_dict.keys():
        s += alpha_dict[i] 
    elif i == " ":
        s += " " 
print(s) 
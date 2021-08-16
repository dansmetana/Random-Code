# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:44:37 2020

@author: dsmet
"""
#written

def encode_file(inputfile, encodedFile):
    import pickle
    dict1 = {}
    with open(inputfile, 'r') as f:
        for k in f:
            dict1 += k #this would likely cause an issue
    with open(encodedFile, 'wb') as e:
        pickle.dump(dict1, e)

def decode_file(encodedFile, decodedFile):
    import pickle
    dict2 = {}
    with open(encodedFile, 'rb') as e:
        dict2 = pickle.load(e)
    with open(decodedFile, 'w') as d:
        d.writelines(dict2)
        
#given


code = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',        'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',        'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',        'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',        'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',        'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',        'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',        'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',        'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',        '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',        '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',        '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',        ':':',',',':':','?':'.','.':'?','<':'>','>':'<',        "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',        '{':'[','[':'{','}':']',']':'}',' ':' '}

def encode(text):
#    encoded = ''
#    for char in text:
#        encoded += str(code[char])   
#    return encoded

    return ''.join([code[char] for char in text])

def decode(text):
#    decoded = ''
#    for char in text:
#        for key in code:
#            if code[key] == char:
#                decoded += key
#    return decoded
    return ''.join([[k for k,v in code.items() if v == c][0] for c in text])

def encode_file1(infile, outfile):
    with open(outfile, 'w') as out_f: 
        with open(infile, 'r') as in_f: 
            for line in in_f:                
                out_f.writelines(encode(line.strip()) + '\n')

def decode_file2(infile, outfile):
    with open(outfile, 'w') as out_f:
        with open(infile, 'r') as in_f:
            for line in in_f: 
                out_f.writelines(decode(line.strip()) + '\n')
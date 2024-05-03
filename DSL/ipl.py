from lark.lark import Lark
from PIL import Image
import numpy as np
from quantize_image import ImageQuantizer
import sys

ipl_grammar = """
    start: statement+

    statement:  NUMBER                                               -> number
               | IDENTIFIER                                          -> id
               | "(" "let" IDENTIFIER "=" statement ")"              -> binding
               | "(" statement MATHOP statement ["mode="MODE] ")"    -> math_operation
               | "(" "load" IDENTIFIER IMAGE ")"                     -> load_image
               | "(" "save" IDENTIFIER IMAGE ")"                     -> save_image
               | "(" "quantize" IDENTIFIER statement ")"             -> quantize

    MATHOP: "+"|"-"|"*"|"/"
    IMAGE: (LETTER|NUMBER|"_")+"."LETTER+
    IDENTIFIER: LETTER(LETTER|NUMBER)*
    MODE: "r"|"g"|"b"|"a"
    
    %import common.LETTER
    %import common.INT -> NUMBER
    %import common.WS
    %ignore WS
"""

parser = Lark(ipl_grammar)
Table = dict()

def addMax255(num1, num2):
    if int(num1) + int(num2) <= 255:
        return num1 + num2
    else:
        return 255

def subMin0(num1, num2):
    if int(num1) - int(num2) >= 0:
        return num1 - num2
    else:
        return 0

def numOpHandler(num1, num2, token):
    return eval(str(num1) + str(token) + str(num2))

def imgProcHandler(data, val, token, mode):
    R,C,D = data.shape
    # print(D)
    newData = np.copy(data)
    if token == '+':
        for r in range(R):
            for c in range(C):
                if mode == 'r' or mode == None:
                    newData[r, c, 0] = addMax255(data[r, c, 0], val)
                if mode == 'g' or mode == None:
                    newData[r, c, 1] = addMax255(data[r, c, 1], val)
                if mode == 'b' or mode == None:
                    newData[r, c, 2] = addMax255(data[r, c, 2], val)
                if mode == 'a':
                    newData[r, c, 3] = addMax255(data[r, c, 3], val)
    elif token == '-':
        for r in range(R):
            for c in range(C):
                if mode == 'r' or mode == None:
                    newData[r, c, 0] = subMin0(data[r, c, 0], val)
                if mode == 'g' or mode == None:
                    newData[r, c, 1] = subMin0(data[r, c, 1], val)
                if mode == 'b' or mode == None:
                    newData[r, c, 2] = subMin0(data[r, c, 2], val)
                if mode == 'a':
                    newData[r, c, 3] = subMin0(data[r, c, 3], val)
    elif token == '*':
        newR = R * val
        newC = C * val
        newData.resize(newR, newC, D)
        for r in range(newR):
            for c in range(newC):
                newData[r, c] = data[int(r / val), int(c / val)]
    elif token == '/':
        newR = int(R / val)
        newC = int(C / val)
        newData.resize(newR, newC, D)
        for r in range(newR):
            for c in range(newC):
                newData[r, c] = data[r * val, c * val]
    return newData

def imgAdd(img1, img2):
    R,C,D = img2.shape
    for r in range(R):
        for c in range(C):
            for d in range(D):
                img1[r,c,d] = addMax255(img1[r,c,d],img2[r,c,d])
    return img1

def imgSub(img1, img2):
    R,C,D = img2.shape
    for r in range(R):
        for c in range(C):
            for d in range(D):
                img1[r,c,d] = subMin0(img1[r,c,d], img2[r,c,d])
    return img1

'''
Interpreter
'''
def interpreter(s):
    if   s.data == 'number':
        return int(s.children[0])
    elif s.data == 'id':
        return Table[s.children[0]]
    elif s.data == 'binding':
        Table[s.children[0]] = interpreter(s.children[1])
        return Table[s.children[0]]
    elif s.data == 'math_operation':
        token = s.children[1]
        leftExp = s.children[0]
        rightExp = s.children[2]
        leftVal = interpreter(leftExp)
        rightVal = interpreter(rightExp)
        try:
            mode = s.children[3]
        except IndexError:
            mode = None
        if type(leftVal) == int and type(rightVal) == int:
            return numOpHandler(leftVal, rightVal, token)
        elif type(leftVal) == np.ndarray and type(rightVal) == int:
            return imgProcHandler(leftVal, rightVal, token, mode)
        elif type(leftVal) == np.ndarray and type(rightVal) == np.ndarray:
            if token == '+':
                return imgAdd(leftVal, rightVal)
            elif token == '-':
                return imgSub(leftVal, rightVal)
            else:
                return "error"
        else:
            return "error"
    elif s.data == 'load_image':
        im = Image.open(s.children[1])
        data = np.asarray(im)
        # print(data.shape)
        Table[s.children[0]] = data
        return data
    elif s.data == 'save_image':
        data = Table[s.children[0]]
        im = Image.fromarray(data)
        im.save(s.children[1])
        return None
    elif s.data == 'quantize':
        data = Table[s.children[0]]
        val = interpreter(s.children[1])
        model = ImageQuantizer(val)
        model.quantize(data)
        quantized_img = model.dequantize()
        return quantized_img


def run_ipl(code):
    ast = parser.parse(code)
    print(ast.pretty())
    for s in ast.children:
        interpreter(s)

'''
Main function for runing the DSL
'''
if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, 'r') as file:
            ipl = file.read()
        run_ipl(ipl)
    else:
        ipl = input("> ")
        run_ipl(ipl)
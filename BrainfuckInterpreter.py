# All valid tokens of the Brainfuck language

# > Increment data pointer
# < Decrement data pointer
# + Add 1 to value in the current cell
# - Subtract 1 from the value in the current cell
# . Output the ASCII character of the current cell's value
# , Input a character and store the ASCII value in the current cell
# [ Beginning of a loop that runs until the value of the data current cell is 0
# ] End of the looping structure
# Also you can use r to reset the memory and data pointer and mi where i is an int between 0-9 to show the memory values


class BrainFuckInterpreter:
    def __init__(self):
        self.memory = [0 for i in range(0, 30000)]
        self.ptr = 0
        self.pos = 0
        self.text = ''

    def eval_token(self):
        token = self.text[self.pos]
        if token == '>':
            self.ptr += 1
            self.pos += 1
        elif token == '<':
            self.ptr -= 1
            self.pos += 1
        elif token == '+':
            self.memory[self.ptr] += 1
            self.pos += 1
        elif token == '-':
            self.memory[self.ptr] -= 1
            self.pos += 1
        elif token == '.':
            print(chr(self.memory[self.ptr]), end='')
            self.pos += 1
        elif token == ',':
            self.memory[self.ptr] = ord(input())
            self.pos += 1
        elif token == '[':
            self.pos += 1
            start_pos = self.pos
            end_pos = 0
            while self.memory[self.ptr] != 0 or self.text[self.pos] != ']':
                if self.text[self.pos] == ']':
                    end_pos = self.pos + 1
                    self.pos = start_pos
                self.eval_token()
            self.pos = end_pos

        elif token == 'r':
            self.memory = [0 for i in range(0, 30000)]
            self.ptr = 0
            self.pos += 1
        elif token == 'm':
            if self.text[self.pos+1] in [str(i) for i in range(0, 10)]:
                [print(self.memory[i]) for i in range(0, int(self.text[self.pos+1]))]
                self.pos += 1
            self.pos += 1
        else:
            raise Exception("Unidentified token: '{}'".format(token))
        print([self.memory[i] for i in range(0, 5)])

    def eval_text(self, text):
        self.text = text
        self.pos = 0
        while self.pos != len(self.text):
            self.eval_token()

bf = BrainFuckInterpreter()
while True:
    code = input("\nbf>>> ")
    bf.eval_text(code)


# Sample Code for Hello World!
# ++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.

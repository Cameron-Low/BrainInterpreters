from PIL import Image

# All valid tokens of the BrainLoller language

# (255, 0, 0, 255) Increment data pointer
# (128, 0, 0, 255) Decrement data pointer
# (0, 255, 0, 255) Add 1 to value in the current cell
# (0, 128, 0, 255) Subtract 1 from the value in the current cell
# (0, 0, 255, 255) Output the ASCII character of the current cell's value
# (0, 0, 128, 255) Input a character and store the ASCII value in the current cell
# (255, 255, 0, 255) Beginning of a loop that runs until the value of the data current cell is 0
# (128, 128, 0, 255) End of the looping structure
# (0, 255, 255, 255) Rotate direction of instruction execution clockwise
# (0, 128, 128, 255) Rotate direction of instruction execution anti-clockwise
# Others NOP


class BrainLollerInterpreter:
    def __init__(self):
        self.memory = [0 for i in range(0, 30000)]
        self.ptr = 0
        self.pos = (0, 0)
        self.dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.dir = 0
        self.image = []
        self.image_width = 0
        self.image_height = 0

    def eval_token(self):
        if self.pos[0] < 0:
            return
        pixel = self.image[self.pos]
        if pixel == (255, 0, 0, 255):
            self.ptr += 1
        elif pixel == (128, 0, 0, 255):
            self.ptr -= 1
        elif pixel == (0, 255, 0, 255):
            self.memory[self.ptr] += 1
        elif pixel == (0, 128, 0, 255):
            self.memory[self.ptr] -= 1
        elif pixel == (0, 0, 255, 255):
            print(chr(self.memory[self.ptr]), end='')
        elif pixel == (0, 0, 128, 255):
            self.memory[self.ptr] = ord(input())
        elif pixel == (255, 255, 0, 255):
            self.pos = (self.pos[0]+1, self.pos[1])
            start_dir = self.dir
            start_pix = self.pos
            end_pix = (0, 0)
            end_dir = 0
            while self.memory[self.ptr] != 0 or self.image[self.pos] != (128, 128, 0, 255):
                if self.image[self.pos] == (128, 128, 0, 255):
                    end_pix = (self.pos[0], self.pos[1])
                    end_dir = self.dir
                    self.pos = start_pix
                    self.dir = start_dir
                self.eval_token()
            self.pos = end_pix
            self.dir = end_dir
        elif pixel == (0, 255, 255, 255):
            self.dir += 1
        elif pixel == (0, 128, 128, 255):
            self.dir -= 1
        else:
            pass
        self.pos = tuple(map(sum, zip(self.pos, self.dirs[self.dir])))
        # Debug memory locations after each pixel evaluation: print([self.memory[i] for i in range(0, 5)])

    def eval_image(self, image_path):
        self.image = Image.open(image_path, 'r')
        self.image_width = self.image.size[0]
        self.image_height = self.image.size[1]
        self.image = self.image.load()
        self.pos = (0, 0)
        while self.pos[0] < self.image_width or self.pos[1] < self.image_height:
            if self.pos[0] < 0 or self.pos[1] < 0 or self.pos[0] >= self.image_width or self.pos[1] >= self.image_height:
                return
            self.eval_token()

bf = BrainLollerInterpreter()
bf.eval_image("HelloWorldSource.png")

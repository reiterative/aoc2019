
class Instruction:
    def __init__(self, pos, source):
        self.opcode = int(source[pos])
        if self.opcode == 99:
            print "End of program"
            print "Data segment:"
            pos = pos + 1
            while pos < len(source):
                print "{}".format(source[pos])
                pos = pos + 1
            return

        self.input1 = int(source[pos+1])
        self.input2 = int(source[pos+2])
        self.output_pos = int(source[pos+3])
        print "opcode: {} input1: {} input2: {} output_pos: {}".format(self.opcode, self.input1, self.input2, self.output_pos)

    def process(self, source):
        exit = 0
        if self.opcode == 1:
            source[self.output_pos] = int(source[self.input1])+int(source[self.input2])
        elif self.opcode == 2:
            source[self.output_pos] = int(source[self.input1])*int(source[self.input2])
        elif self.opcode == 99:
            exit = 1
        else:
            print "Invalid opcode: ({})".format(self.opcode)
        return exit

def read_instruction(pos, source):
    return Instruction(pos, source)

with open('input-day2') as fp:

    line = fp.readline()
    while line:
        starting_instructions = line.split(',')
        exit = 0
        pos = 0
        print "Processing..."

        noun = 0
        verb = 0
        for noun in range(99):
            for verb in range(99):
            instructions = starting_instructions
            instructions[1] = noun
            instructions[2] = verb
            while exit == 0:
                i = read_instruction(pos, instructions)
                exit = i.process(instructions)
                pos = pos + 4

            if target = 19690720
                target_noun = noun
                target_verb = verb
                noun = 99
                verb = 99

       print "Results"
       exit = 0
       pos = 0
       while exit == 0:
           i = read_instruction(pos, instructions)
           if i.opcode == 99:
               exit = 1
           pos = pos + 4

       line = fp.readline()

print "noun = {} verb = {}".format(target_noun, target_verb)
print "Finished ({}):".format(pos)
fp.close()

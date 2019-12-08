
class Instruction:
    def __init__(self, pos, source):
        self.opcode = int(source[pos])
        if self.opcode != 99:
            self.input1 = int(source[pos+1])
            self.input2 = int(source[pos+2])
            self.output_pos = int(source[pos+3])

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

    def debug_print(self, pos, source):
        if self.opcode == 99:
            print "End of program"
            print "Data segment:"
            pos = pos + 1
            while pos < len(source):
                print "{}".format(source[pos])
                pos = pos + 1
        else:
            print "opcode: {} input1: {} input2: {} output_pos: {}".format(self.opcode, self.input1, self.input2, self.output_pos)

def run_program(source, noun, verb):
    instructions = list(source)
    instructions[1] = noun
    instructions[2] = verb
    exit = 0
    pos = 0
    while exit == 0:
        i = Instruction(pos, instructions)
        exit = i.process(instructions)
        pos = pos + 4

    result = int(instructions[0])
    print "noun={} verb={} result={}".format(noun, verb, result)
    return result

# main method
with open('input-day2') as fp:
    line = fp.readline()
    starting_instructions = line.split(',')
    print "Testing..."
    result = run_program(starting_instructions, 12, 2)
    if result == 4090701:
        print "Processing..."
        noun = 0
        for noun in range(100):
            verb = 0
            for verb in range(100):
                result = run_program(starting_instructions, noun, verb)
                if result == 19690720:
                    target_noun = noun
                    target_verb = verb
                    noun = 99
                    verb = 99

print "target_noun = {} target_verb = {}".format(target_noun, target_verb)
print "Finished"
fp.close()

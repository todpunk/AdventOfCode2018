from days import AOCDay, day


@day(2)
class DayOne(AOCDay):
    def part1(self, input_data):
        threes = 0
        twos = 0

        for id in input_data:
            counts = {}
            found_two = False
            found_three = False
            for char in id:
                if char not in counts:
                    counts[char] = 0
                counts[char] += 1
            for key, val in counts.items():
                if val == 2:
                    found_two = True
                elif val == 3:
                    found_three = True
            if found_three:
                threes += 1
            if found_two:
                twos += 1
        
        yield threes * twos

    def part2(self, input_data):
        input_data = sorted(input_data)
        a, b = input_data[:-1], input_data[1:]
        word_size = len(a[0])
        box_a = None
        box_b = None
        for i in range(len(a)):
            off_by = 0
            for x in range(word_size):
                if a[i][x] != b[i][x]:
                    off_by += 1
                if off_by >= 2:
                    break
            if off_by == 1:
                box_a = a[i]
                box_b = b[i]
        answer = ""
        for i in range(word_size):
            if box_a[i] == box_b[i]:
                answer = answer + box_a[i]
        yield answer

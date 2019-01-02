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
        raise NotImplementedError()

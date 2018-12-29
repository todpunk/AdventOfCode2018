from days import AOCDay, day


@day(1)
class DayOne(AOCDay):
    def part1(self, input_data):
        sum = 0
        for input in input_data:
            sum = sum + int(input)
        yield sum

    def part2(self, input_data):        
        daFrequency = 0
        unique_frequencies = set()

        while True:
            for i in input_data:
                i = int(i)
                if daFrequency in unique_frequencies:
                    yield daFrequency
                    return
                unique_frequencies.add(daFrequency)
                daFrequency += i

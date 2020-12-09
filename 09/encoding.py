import itertools 
import copy

with open(f'09/input.txt') as course:
    entries = [int(line.strip()) for line in course]

orignetries = entries[:]

def find_error(input, preamblesize):
    entries = input
    is_looping = True
    for z in range(len(input)):
        lookback, searchspace = entries[:preamblesize], entries[preamblesize:]
        print('lookback is ' + str(lookback))
        print('searchspace is ' + str(searchspace))
        # lookbacksums = list(set(list(itertools.chain.from_iterable([[y+i for y in lookback] for i in lookback]))) - set([y + y for y in lookback]))
        alllookbacksums = list(itertools.chain.from_iterable([[y+i for y in lookback] for i in lookback]))
        dupes = [y + y for y in lookback]
        print('all sums are ' + str(alllookbacksums))
        print('dupes are ' + str(dupes))
        for z in dupes:
            if z in alllookbacksums:
                alllookbacksums.remove(z)
        print('all sums is now ' + str(alllookbacksums))
        # for y in lookback:
        #     [lookbacksums.append(y+x) for x in lookback]
        # print(lookbacksums)
        # entries.pop(0)
        if searchspace[0] not in alllookbacksums:
            print(str(searchspace[0]) + " is bad!")
            break
        entries.pop(0)
        
"""         for num in searchspace:
            if num not in alllookbacksums:
                print(str(num))
                print('!!!!!!!!!!!11')
                is_looping = False
                break
        if not is_looping:
            break """

def xmas2(input, target):
    
    for x in range(len(input)): # check each number in the input and save it as the starting number x
        sum = 0  # for each new starting number, reset the sum to 0
        for y in range(x,len(input)): # check each number in the input from the position of the starting number onward
            sum += input[y] # add the number y from the inner loop to the sum
            if sum > target: # check if the sum is bigger than our target. If yes, break and use the next starting number
                break 
            elif sum == target: # if the sum is equal to our target
                number_list = input[x:y+1] # save the contiguous set to number_list
                print(str(number_list))
                return(min(number_list)+max(number_list)) # return the smallest element added to the biggest element in number_list

def part2(xs, p1):
    for i in range(len(xs)):
        x0 = xs[i]
        su,mi,ma = x0,x0,x0
        for j in range(i + 1, len(xs)):
            x = xs[j]
            su,mi,ma = (su + x), (mi if mi < x else x), (ma if ma > x else x)
            if su > p1:
                break
            if su == p1:
                return mi + ma

testentries = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
find_error(entries, 25)
print(xmas2(testentries, 127))
print(xmas2(orignetries, 507622668)) # doesn't work?
import code; code.interact(local=locals()) 
print(part2(orignetries, 507622668))

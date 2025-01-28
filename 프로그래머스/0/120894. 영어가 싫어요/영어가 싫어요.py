def solution(numbers):
    num_dict = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
    new_numbers = []
    temp = ""
    for num in numbers:
        temp += num
        if temp in num_dict:
            new_numbers.append(temp)
            temp = ""
    answer = []
    nums = {"zero" : '0', "one" : '1', "two" : '2', "three" : '3', "four" : '4', "five" : '5', "six" : '6', "seven" : '7', "eight" : '8', "nine" : '9'}
    for new_num in new_numbers:
        if new_num in nums:
            answer.append(nums.get(new_num))
    return int(''.join(answer))

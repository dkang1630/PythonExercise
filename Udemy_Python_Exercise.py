'''
def titleize(words):
    words_list = words.split()
    cap_words = []
    for words in words_list:
        cap_words.append(words[0].upper() + words[1:]) 
    cap = ' '.join(cap_words)
    return cap

print(titleize("hELLlo this"))
'''
'''
def find_factors(num):
    factor_lst = []
    for i in range(num):
        if num % (i+1) == 0:
            factor_lst.append(i+1)
    return factor_lst

print(find_factors(56))

'''
'''
def includes(item, val, start=None):
    if type(item) == dict:
        return val in item.values()
    if start is None:
        return val in item
    return val in item[start:]

print(includes({ 'a': 1, 'b': 2 }, 'a'))
'''
'''
def repeat(str, num):
    output_list = []
    for i in range(num):
        output_list.append(str)
    final = ''.join(output_list)
    return final

print(repeat('abc', 2))
'''
'''
def two_list_dictionary(lst1, lst2):
    dict = {}
    for key in range(len(lst1)):
        if (key+1) > len(lst2):
            dict[lst1[key]] = None
        else:
            dict[lst1[key]] = lst2[key]
    return dict
        
print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))
'''
'''
def range_in_list(lst, start=0, end=None):
    end = end or lst[-1]
    return sum(lst[start:end+1])

print(range_in_list([1,2,3,4],0,2)) #  6
print(range_in_list([1,2,3,4]))
print(range_in_list([1,2,3,4],0,100)) # 10
'''
'''
def same_frequency(num1, num2):
    match = 0
    str_num_1 = str(num1)
    str_num_2 = str(num2)
    for num_1 in str_num_1:
        if num_1 in str_num_2:
            match += 1
    if match == len(str_num_1):
        return True
    else:
        return False

print(same_frequency(551122,221515))
# print(same_frequency(321142,3212215))
# print(same_frequency(1212, 2211))   
'''
'''
def nth(lst, num):
    return lst[num]

print(nth(['a', 'b', 'c', 'd'], 1))
'''
'''
def find_the_duplicate(lst):
    sorted_lst = sorted(lst)
    prev_num = None
    for num in sorted_lst:
        if num == prev_num:
            return num
        else:
            prev_num = num
    return None

print(find_the_duplicate([1,2,1,4,3,12]))
'''   
'''
list1 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

def sum_up_diagonals(lst):
    total = 0
    
    for i, value in enumerate(lst):
        total += lst[i][i]
        print(total)
        total += lst[i][-1-i]
        print(total)

    return total

print(sum_up_diagonals(list1))
'''  
'''
def min_max_key_in_dictionary(dic):
    min_key = min(dic.keys())
    max_key = max(dic.keys())
    return [min_key, max_key]

print(min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}))

'''
'''
def find_greater_numbers(lst):
    count = 0
    
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j] > lst[i]:
                count += 1
    return count

print(find_greater_numbers([5,4,3,2,1]))    

'''
'''
def two_oldest_ages(lst):
    oldest = max(lst)
    second = 0
    new_list = [num for num in lst if num != oldest]
    for i in new_list:
        if i > second:
            second = i
    return [second, oldest]

print(two_oldest_ages([6,1,9,10,4]))
'''
'''
def is_odd_string(str):
    length = len(str) 
    total = 0
    for num in range(1, length + 1):
        total += num
        print(total)
    print(total)
    if total % 2 == 1:
        return True
    return False
    
print(is_odd_string('amazing'))
'''

def valid_parentheses(str):
    if str[0] == ')':
        return False
    for i in str:
        if (i + 1) % 2 == 1:
            if str[i] == '(':
                first_P_Count += 1
        else:
            if str[i] == ')':
                second
                        

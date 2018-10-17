'''quick sort in place
>>> lst = [5, 2, 1, 15, 10]
>>> print(quick_sort(lst))
[1, 2, 5, 10, 15]
>>> lst2 = [4, 6, 2, 3, 7 , 5, 10, 45, 23, 56, 89, 0]
>>> print(quick_sort(lst2))
[]



'''

def quick_sort(lst):



    import random

    def _quick_sort(lst, first, last):


        pivot = lst[(first + last)//2]
        

        #l - left index
        #r - right index

        l = first
        r = last
        left_found = False
        right_found = False
       
        print(l, r, pivot)
        while l != r:
            print(l, r, pivot)
            print(lst)
            if lst[l] >= pivot:
                
                left_found= True
            else:
                l += 1
            if lst[r] <= pivot:
                
                right_found = True
            else:
                r -= 1
            if left_found and right_found:
                print('hi')
                lst[l], lst[r] = lst[r],lst[l]
                left_found = right_found = False
            
        if first != l:
            _quick_sort(lst, first, l - 1)
        if l != last:
            _quick_sort(lst, l+1, last)
        
            
        
    print(len(lst)-1)
    _quick_sort(lst, 0, len(lst)-1)
    
    

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")       

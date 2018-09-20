'''You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

>>> get_products_of_all_ints_except_at_index([1, 7, 3, 4])
[84, 12, 28, 21]

Here's the catch: You can't use division in your solution!'''

def get_products_of_all_ints_except_at_index(lst):

    
    product_befor_indx = []
    product_after_indx = []
    products_of_all_ints_except_at_indx = []


    current_product = 1
    product_befor_indx.append(current_product)
    
    for i in range(1, len(lst)):
        current_product *= lst[i-1]
        product_befor_indx.append(current_product)

    current_product = 1
    product_after_indx.append(current_product)

    for i in range(len(lst)-2, -1, -1):
        current_product *= lst[i+1]
        product_after_indx.append(current_product)

    #print(lst, product_befor_indx, product_after_indx)

    for i in range(len(product_befor_indx)):
        products_of_all_ints_except_at_indx.append(product_befor_indx[i] * product_after_indx[len(product_after_indx)-1-i])

    return products_of_all_ints_except_at_indx













if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print('\n***TST PASSES***\n')
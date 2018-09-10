'''
Your company built an in-house calendar tool called HiCal. 
You want to add a feature to see the times in a day when everyone is available.
To do this, you’ll need to know when any team is having a meeting. 
In HiCal, a meeting is stored as a tuple ↴ of integers (start_time, end_time).
These integers represent the number of 30-minute blocks past 9:00am.

For example:

(2, 3)  # Meeting from 10:00 – 10:30 am
(6, 9)  # Meeting from 12:00 – 1:30 pm

Write a function merge_ranges() that takes a list of multiple meeting time ranges
and returns a list of condensed ranges.

For example, given:

  
  >>> merge_ranges ([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
  [(0, 1), (3, 8), (9, 12)]


'''
def merge_ranges(meetings):

    #sort list by start time - O(nlogn)
    sorted_meetings = sorted(meetings)

    merged_list = [sorted_meetings[0]]

    for current_start_time, current_end_time in sorted_meetings[1:]:
        last_merged_start, last_merged_end = merged_list[-1]

        if last_merged_end >= current_start_time:
            merged_list[-1] = (last_merged_start, max(last_merged_end, current_end_time))
        else:
            merged_list.append((current_start_time, current_end_time))

    return merged_list


    





if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED! GO GO GO!\n")
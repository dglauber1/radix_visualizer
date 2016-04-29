def print_buckets(buckets, ordered_place):
    """print_buckets: array, int -> 
    Purpose: prints the contents of a 2D array representing the buckets of a radix sort algorithm
    Consumes: buckets - an array of int arrays, where the xth int array contains all integers with the digit x at ordered_place
              ordered_place - a power of 10 representing the current place that the integers have been sorted on
    Produces: nothing
    """
    index_string = '| '
    for i in range(len(buckets)):
        sub_idx_str = ''
        bucket_size = len(buckets[i])
        if (bucket_size > 0):
            sub_idx_str += ' ' * (2 * bucket_size - 1)
        else:
            sub_idx_str += ' '
        middle_index = len(sub_idx_str) / 2
        sub_idx_str = sub_idx_str[:middle_index] + str(i) + sub_idx_str[middle_index + 1:]
        index_string += sub_idx_str + ' | '
    to_print = index_string + 'bucket index'
    to_print = '~' * len(index_string) + '\n' + to_print
    
    place = 1
    while True:
        do_break = True
        next_line = '| '
        for bucket in buckets:
            if len(bucket) < 1:
                next_line += ' ' * 2
            else:
                for number in bucket:
                    digit = ''
                    if number >= place:
                        do_break = False
                        digit = str(number % (place * 10) / place)
                    else:
                        digit = ' '
                    next_line += digit + ' '
            next_line += '| '
        if do_break:
            break
        if ordered_place == place:
            next_line += '<- ' + str(place) + '\'s place has been sorted'
        to_print = next_line + '\n' + to_print
        place *= 10

    print to_print + '\n'
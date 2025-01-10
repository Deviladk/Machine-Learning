for x in range(102,499):
    digit_str=str(x)+str(2*x)+str(3*x)
    digit_len=len(digit_str)
    digit_set_len=len(set(digit_str))
    if(digit_len==digit_set_len):
        print(x,2*x,3*x,digit_str,digit_len,digit_set_len)
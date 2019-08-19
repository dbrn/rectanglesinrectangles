# Dobi is solving a logical reasoning book to prepare for her upcoming 
# examinations. She comes across a question in which she is given X horizontal 
# lines and Y vertical lines. These lines intersect and create some rectangles. 
# She needs to count all the rectangles in the figure. Dobi is a little stupid 
# and needs your help to figure this problem out. 
# Help Dobi by writing a code to solve this problem.
# Note: Lines go infinitely in both directions.
test_cases = int(input())
for case in range(test_cases):
    # input the number of horizontal and vertical lines in a single input
    # and cast every entry to integer. By subtracting 1, we find the base and
    # height of the rectangle they draw.
    rectangles = 0 # this var is the number of rectangles and sub-rectangles.
    x_y = tuple(map(lambda x: int(x), input().split()))
    base = x_y[0] - 1
    height = x_y[1] - 1
    # calculate and sum every rectangle of every possible area that can fit
    # inside our main rectangle:
    # 1x1 = base * height
    # 1x2 = base * (height -1)
    # (...)
    # 2x1 = (base - 1) * height
    # 2x2 = (base - 1) * (height -1)
    # (...)
    for b in range(base, 0, -1):
        for h in range (height, 0, - 1):
            rectangles += b * h
    print(rectangles)

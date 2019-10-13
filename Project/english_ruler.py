"""
Consider of a typical English ruler as below, demonstrates several such rulers
with varying major tick lengths (although not drawn to scale).

---- 0              ----- 0             --- 0
-                   -                   -
--                  --                  --
-                   -                   -
---                 ---                 --- 1
-                   -                   -
--                  --                  --
-                   -                   -
---- 1              ----                --- 2
-                   -                   -
--                  --                  --
-                   -                   -
---                 ---                 --- 3
-                   -
--                  --
-                   -
---- 2              ----- 1
(a)                 (b)                 (c)

Three sample outputs of an English ruler drawing:
(a) a 2-inch ruler with major tick length 4.
(b) a 1-inch ruler with major tick length 5.
(c) a 3-inch ruler with major tick length 3.

"""


def draw_line(tick_length, tick_label = ""):
    """Draw on line with given tick length (follow by optional label).
    :param tick_length: the len of tick.
    :param tick_label: the tick label description(optional).
    """
    line = "-" * tick_length
    if tick_label:
        line += " " + tick_label
    print(line)

def draw_interval(tick_length):
    """Draw tick interval baseed upon a central tick lengh.
    :param tick_length: the length of major tick.
    """
    if tick_length > 0:

        # Draw top tick
        draw_interval(tick_length - 1)

        # Draw center
        draw_line(tick_length)

        # Draw bottom tick
        draw_interval(tick_length - 1)

def draw_ruler(length_inch, tick_length):
    """Draw English ruler with a given number of lenth in inches and tick
    length,
    :param length_inch: the length of ruler in inches.
    :param the length of tick lebel.
    """
    draw_line(tick_length, '0')
    for i in range(1, length_inch + 1):
        draw_interval(tick_length-1)
        draw_line(tick_length, str(i))

if __name__ == "__main__":
    draw_ruler(3, 5)


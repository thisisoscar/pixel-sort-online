# pixel-sort-online

This code is a pixel sorter, and may I add, one of the best pixel sorters I've seen. It's still got a way to go to be perfect but it's much closer than what I've seen on youtube. When I say sort pixels, you can do it mathematically where all the reddest ones go first then all the greenest ones then all the bluest ones, but that doesn't look right. If I saw a "sorted" image from that method with no other context, I wouldn't say that it's sorted because theres massively different pixels next to each other, which a proper pixel sorting algorithm wouldn't have. It took a few days to find the current algorithm, which is just a lexicographic order in the hsv colour model in the order h, v, s. Basically, it's sorted by hue, then if there is more than one colour with the same hue it sorts them by value and again by saturation if there are any pixels with the same hue and value. I've sorted two identical (ish) images with the normal rgb and my hvs to see the difference. Both images have one pixel for every possible colour in their colour model.

sorted by rgb:
![sorted by rgb](<images/rgb sorted.png>)

sorted by hvs:
![sorted by hvs](<images/hsv sorted.png>)

The rgb sort looks more random with all the green mixed with the blue and the red at the bottom is drowned out by the other two still. In my one you have the expected bands of colours and looks a lot less random. Each 256x16 box that they inevitably create has only one colour of varying values and saturations, much more sorted than rgb's boxes which usually have all three colours in them. It can still be made better by pushing the darker and lighter shades to the top and bottom but I'm not sure how to do that in code and I'm not too bothered but I'll update the code if I think up a solution.

# Quick
The quick.py file sorts the image behind the scenes, showing you the sorted image at the end.

# Visual
The visual.py file outputs the image while it's being sorted so you can see it work. It's much much slower than quick.py, I'll add more sorting algorithms eventually. 
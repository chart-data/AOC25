# Advent of Code Day 1

# Dial Starts point at 50
dial = 50


# How many full rotations there were (e.g. if input is R678 then we just add
# 6 to sum_full and pretend then input was R78
sum_full = 0

# Count of times dial points to zero
total = 0


f = open('input.txt')


while True:
   line = f.readline()

   if (len(line)) == 0:
      break

   dir = line[:1]
   in_shift = int(line[1:])

# Kill the excess rotations before they start...
# Except for part 2 we have to keep track.  Let's pull out those rotations seperately

   full_rots = in_shift // 100
   shift     = in_shift % 100

#   if (((full_rots*100) + shift) != in_shift):
#      print ('Mod arithmetic did not do what we thought', in_shift, full_rots, shift)
#      quit()

   sum_full = sum_full + full_rots

   prev_dial = dial

   if dir == 'L':
      dial = dial - shift
   else:
      dial = dial + shift

# Dial should now be between -99 and 198
# Not sure we trust mod on -ve numbers, so let's do it the long way
# And if it's outside {0,99} we probably passed through zero

   thru = 0
   match = 0

   if (dial==0):
      match = 1
   elif (dial < 0):
      dial = dial + 100
      if (prev_dial != 0):
         thru = 1
   elif (dial > 99):
      dial = dial - 100
      thru = 1

   total = total + full_rots + match + thru

#   print(line, 'New dial ', dial, ' full rots ', full_rots, ' passes ', thru, ' matches ', match)

print(total)


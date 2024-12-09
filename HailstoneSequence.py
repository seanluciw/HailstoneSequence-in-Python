# HailstoneSequence.py
# by Sean Luciw Nov. 23 2024

'''
My implementation of the famous 3x+1 scenario

inspired by this video:
https://www.youtube.com/watch?v=094y1Z2wpJg&t=589s

WISHLIST ITEMS:
-accept negative numbers
-format parity sequence
-user can choose file output
-show ratio of max/start
-show ratio of odd/even as percentage pair
-in range mode, show average of stop ratios
-question: at what step number does the value first fall below the start number
--and subsequent downward crossings
'''

import math
import time

#import sys
#orig_stdout = sys.stdout
#f = open('HailstoneSequence_out.txt', 'w')
#sys.stdout = f

def func_hailstone(var_int_start_num, var_detailed_bool, var_range_mode_bool):
	var_current_value = var_int_start_num
	var_next_value = var_current_value # required for start = 1 scenario
	var_max_value = 0
	var_stopping_time = 0
	#
	var_step_of_max_val = 0
	#
	if (var_detailed_bool) and (not var_range_mode_bool):
		var_count_even = 0
		var_count_odd = 0
		var_count_starts_with_one = 0
		var_count_starts_with_two = 0
		var_count_starts_with_three = 0
		var_count_starts_with_four = 0
		var_count_starts_with_five = 0
		var_count_starts_with_six = 0
		var_count_starts_with_seven = 0
		var_count_starts_with_eight = 0
		var_count_starts_with_nine = 0
		var_hailstone_number_seq_str = '\nHAILSTONE NUMBER SEQUENCE:\n'
		var_hailstone_parity_seq_str = '\nHAILSTONE PARITY SEQUENCE:\n'
	while True:
		# ODD
		if (var_current_value % 2) and (var_current_value != 1):
			var_next_value = int(3 * var_current_value + 1)
			var_stopping_time = var_stopping_time + 1
			if (var_detailed_bool) and (not var_range_mode_bool):
				var_hailstone_number_seq_str = var_hailstone_number_seq_str + str(var_current_value) + ','
				var_count_odd = var_count_odd + 1
				var_hailstone_parity_seq_str = var_hailstone_parity_seq_str + 'O'
		# EVEN
		elif var_current_value != 1:
			var_next_value = int(var_current_value / 2)
			var_stopping_time = var_stopping_time + 1
			if (var_detailed_bool) and (not var_range_mode_bool):
				var_hailstone_number_seq_str = var_hailstone_number_seq_str + str(var_current_value) + ','
				var_count_even = var_count_even +1
				var_hailstone_parity_seq_str = var_hailstone_parity_seq_str + 'E'
		#
		var_max_value = max(var_next_value, var_current_value, var_max_value)
		#
		if var_max_value == var_next_value:
			var_step_of_max_val = var_stopping_time
		#
		if (var_detailed_bool) and (not var_range_mode_bool):
			var_first_digit = int(str(var_current_value)[0])
			if var_first_digit == 1:
				var_count_starts_with_one = var_count_starts_with_one + 1
			elif var_first_digit == 2:
				var_count_starts_with_two = var_count_starts_with_two + 1
			elif var_first_digit == 3:
				var_count_starts_with_three = var_count_starts_with_three + 1
			elif var_first_digit == 4:
				var_count_starts_with_four = var_count_starts_with_four + 1
			elif var_first_digit == 5:
				var_count_starts_with_five = var_count_starts_with_five + 1
			elif var_first_digit == 6:
				var_count_starts_with_six = var_count_starts_with_six + 1
			elif var_first_digit == 7:
				var_count_starts_with_seven = var_count_starts_with_seven + 1
			elif var_first_digit == 8:
				var_count_starts_with_eight = var_count_starts_with_eight + 1
			elif var_first_digit == 9:
				var_count_starts_with_nine = var_count_starts_with_nine + 1
		# incrementation
		var_current_value = var_next_value
		# IF REACHED END OF HAILSTONE 4-2-1 LOOP
		if var_next_value == 1:
#			sys.stdout = f
			# this ratio has +1 indexing which is different from 'stopping time'. This adjustment makes  most sense when looking at small starting numbers like 1 or 2.
			var_position_ratio_of_max_val = (var_step_of_max_val + 1) / (var_stopping_time + 1)
			if (var_range_mode_bool):
				if (var_detailed_bool):
					print("{0:<23} {1:<23} {2:<23} {3:<23} {4:<23,.8f}".format(var_int_start_num, var_stopping_time, var_max_value, var_step_of_max_val, var_position_ratio_of_max_val))
				return var_int_start_num, var_stopping_time, var_max_value
			else:
				print('\nOUTPUT:')
				print('Starting number input:', var_int_start_num)
				print('Total stopping time:', var_stopping_time,'steps')
				print('Maximum value:', var_max_value)
				print('Step number of maximum value:', var_step_of_max_val)
				print('Position ratio of maximum value', round(var_position_ratio_of_max_val, 8))
				if (var_detailed_bool):
					var_hailstone_number_seq_str = var_hailstone_number_seq_str + str(var_current_value)
					var_count_odd = var_count_odd + 1
					if var_int_start_num != 1:
						var_count_starts_with_one = var_count_starts_with_one + 1
					var_hailstone_parity_seq_str = var_hailstone_parity_seq_str + 'O'
					print('Odd number count:', var_count_odd)
					print('Even number count:', var_count_even)
					print('Numbers starting with 1:', var_count_starts_with_one, '=', round(100 * var_count_starts_with_one / (var_stopping_time + 1),2) ,'%')
					print('Numbers starting with 2:', var_count_starts_with_two, '=', round(100 * var_count_starts_with_two / (var_stopping_time + 1),2) ,'%')
					print('Numbers starting with 3:', var_count_starts_with_three, '=', round(100 * var_count_starts_with_three / (var_stopping_time + 1),2) ,'%')
					print('Numbers starting with 4:', var_count_starts_with_four, '=', round(100 * var_count_starts_with_four / (var_stopping_time + 1),2) ,'%')
					print('Numbers starting with 5:', var_count_starts_with_five, '=', round(100 * var_count_starts_with_five / (var_stopping_time + 1),2) ,'%')
					print('Numbers starting with 6:', var_count_starts_with_six, '=', round(100 * var_count_starts_with_six / (var_stopping_time + 1),2) ,'%')
					print('Numbers starting with 7:', var_count_starts_with_seven, '=', round(100 * var_count_starts_with_seven / (var_stopping_time + 1),2) ,'%')
					print('Numbers starting with 8:', var_count_starts_with_eight, '=', round(100 * var_count_starts_with_eight / (var_stopping_time + 1),2) ,'%')
					print('Numbers starting with 9:', var_count_starts_with_nine, '=', round(100 * var_count_starts_with_nine / (var_stopping_time + 1),2) ,'%')
					print('(the above percentages relate to Benford\'s Law)')
					print(var_hailstone_number_seq_str)
					print(var_hailstone_parity_seq_str)
	#			sys.stdout = orig_stdout
			break

def func_main_loop():
	print('\nHailstone Sequence program written by Sean Luciw Nov. 23, 2024.\nThis program doesn\'t attempt to disprove the Collatz Conjecture, merely view numerical output.\nIf the number is ODD, the next number will be 3x+1. If the number is EVEN, the next number is x/2. \nThe process terminates when 1 is reached because that is where the loop 1-4-2 is encountered. \nPositive starting number only.')
	msg_user_input_start_num = '\nINPUT:\nEnter starting number or [R] for Range Mode: '
	while True:
		user_response = input(msg_user_input_start_num)
		# start of RANGE MODE
		if user_response.upper() == 'R':
			print('\nRANGE MODE')
			var_max_stopping_time = 0
			var_max_time_start_num_array = []
			var_max_max_value = 0
			var_max_val_start_num_array = []
			msg_user_input_range_start = 'Enter lowest starting number: '
			while True:
				user_response_range_start = input(msg_user_input_range_start)
				if (user_response_range_start.isdigit()) and (int(user_response_range_start) != 0):
					break
				else:
					print('ERROR: TRY AGAIN')
			msg_user_input_range_end = 'Enter highest starting number: '
			while True:
				user_response_range_end = input(msg_user_input_range_end)
				if (user_response_range_end.isdigit()) and (int(user_response_range_end) > int(user_response_range_start)):
					break
				else:
					print('ERROR: TRY AGAIN')
			msg_user_response_detailed = 'Enter [D] for detailed output or [S] for simple: '
			while True:
				user_response_detailed_simple = input(msg_user_response_detailed)
				if (user_response_detailed_simple.upper() == 'D'):
					var_detailed = True
					break
				elif (user_response_detailed_simple.upper() == 'S'):
					var_detailed = False
					break
				else:
					print('ERROR: TRY AGAIN')
			print('\nOUTPUT:')
			if (var_detailed):
				var_output_headings_str = ("{0:<23} {1:<23} {2:<23} {3:<23} {4:<23}".format('START NUMBER', 'STOPPING TIME', 'MAXIMUM VALUE', 'STEP NUM OF MAX VALUE', 'POSITION RATIO OF MAX VALUE'))
				print(var_output_headings_str)
			for var_start_num in range (int(user_response_range_start), int(user_response_range_end) + 1):
				var_this_start_num, var_this_stopping_time, var_this_max_value = func_hailstone(int(var_start_num), var_detailed, True)

				if (var_this_max_value >= var_max_max_value):
					if (var_this_max_value == var_max_max_value):
						var_max_val_start_num_array.append(str(var_this_start_num))
					else:
						var_max_val_start_num_array = [str(var_this_start_num)]
					var_max_max_value = var_this_max_value
					
				if (var_this_stopping_time >= var_max_stopping_time):
					if (var_this_stopping_time == var_max_stopping_time):
						var_max_time_start_num_array.append(str(var_this_start_num))
					else:
						var_max_time_start_num_array = [str(var_this_start_num)]
					var_max_stopping_time = var_this_stopping_time
			if (var_detailed):
				print(var_output_headings_str)
				print('')
			var_output_highest_max_str = ('The starting number(s) of ' + (', '.join(var_max_val_start_num_array)) +  ' reached the highest maximum value of ' + str(var_max_max_value) + '.')
			var_output_longest_stop_str = ('The starting number(s) of ' + (', ' .join(var_max_time_start_num_array)) + ' had the longest stopping time of ' + str(var_max_stopping_time) + '.')
			print (var_output_highest_max_str)
			print (var_output_longest_stop_str)
			print('')
			break
		# end of RANGE MODE, start of INDIVIDUAL MODE
		elif user_response.isdigit(): # this doesn't accept negative numbers
			msg_user_response_detailed = 'Enter [D] for detailed output or [S] for simple: '
			while True:
				user_response_detailed_simple = input(msg_user_response_detailed)
				if (user_response_detailed_simple.upper() == 'D'):
					var_detailed = True
					break
				elif (user_response_detailed_simple.upper() == 'S'):
					var_detailed = False
					break
				else:
					print('ERROR: TRY AGAIN')
			print('')
			func_hailstone(int(user_response), var_detailed, False) # detailed, range mode
			print('')
			break
		else:
			print('ERROR: TRY AGAIN')

func_main_loop()

#sys.stdout = orig_stdout
#f.close()

'''
Created by: Roman Beya
Created on: 14-oct-2017
Created for: ICS3U
This program calculates the cost of pizza depending on size, # of toppings, with and without HST
'''
import ui

LARGE_PIZZA = 6
EXTRA_LARGE_PIZZA = 10
TOPPING_1 = 1
TOPPING_2 = 1.75
TOPPING_3 = 2.50
TOPPING_4 = 3.25
HST = 1.13

def calculate_pizza_cost_touch_up_inside(sender):
	# calculates which pizza the user wants to buy plus toppings, with and without HST
	if int(view['pizza_size_textfield'].text) == 1: # They have selected a large pizza
		# Calculating cost without HST first, then calculates costs with HST second
		if int(view['#_of_toppings_textfield'].text) == 0:
			cost1_without_HST = (LARGE_PIZZA) # If they order 0 toppings
			cost1_with_HST = (LARGE_PIZZA) * HST 
			HST_difference = cost1_with_HST - cost1_without_HST
			view['final_costs_label'].text = "Sub Total = ${:,.2F}\nHST = ${:,.2F}\nFinal Cost = ${:,.2F}".format(cost1_without_HST, HST_difference, cost1_with_HST)
		
		elif int(view['#_of_toppings_textfield'].text) == 1:
			cost2_without_HST = (LARGE_PIZZA + TOPPING_1)	
			cost2_with_HST = (LARGE_PIZZA + TOPPING_1) * HST
			HST_difference = cost2_with_HST - cost2_without_HST
			view['final_costs_label'].text = "Sub Total = ${:,.2F}\nHST = ${:,.2F}\nFinal Cost = ${:,.2F}".format(cost2_without_HST, HST_difference, cost2_with_HST)
		
		elif int(view['#_of_toppings_textfield'].text) == 2:
			cost3_without_HST = (LARGE_PIZZA + TOPPING_2)
			cost3_with_HST = (LARGE_PIZZA + TOPPING_2) * HST
			HST_difference = cost3_with_HST - cost3_without_HST
			view['final_costs_label'].text = "Sub Total = ${:,.2F}\nHST = ${:,.2F}\nFinal Cost = ${:,.2F}".format(cost3_without_HST, HST_difference, cost3_with_HST)
			
		elif int(view['#_of_toppings_textfield'].text) == 3:
			cost4_without_HST = (LARGE_PIZZA + TOPPING_3) 
			cost4_with_HST = (LARGE_PIZZA + TOPPING_3) * HST 
			HST_difference = cost4_with_HST - cost4_without_HST
			view['final_costs_label'].text = "Sub Total = ${:,.2F}\nHST = ${:,.2F}\nFinal Cost = ${:,.2F}".format(cost4_without_HST, HST_difference, cost4_with_HST)
		
		elif int(view['#_of_toppings_textfield'].text) == 4:
			cost5_without_HST = (LARGE_PIZZA + TOPPING_4)
			cost5_with_HST = (LARGE_PIZZA + TOPPING_4) * HST
			HST_difference = cost5_with_HST - cost5_without_HST
			view['final_costs_label'].text = "Sub Total = ${:,.2F}\nHST = ${:,.2F}\nFinal Cost = ${:,.2F}".format(cost5_without_HST, HST_difference, cost5_with_HST)
			
	# EXTRA Large Pizza
	if int(view['pizza_size_textfield'].text) == 2: # They have selected a EXTRA large pizza
		# Calculating cost without HST first, then calculates costs with HST second
		if int(view['#_of_toppings_textfield'].text) == 0:
			cost1_without_HST = (EXTRA_LARGE_PIZZA) # If they order 0 toppings
			cost1_with_HST = (EXTRA_LARGE_PIZZA) * HST 
			HST_difference = cost1_with_HST - cost1_without_HST
			view['final_costs_label'].text = "Sub Total = ${:,.2F}\nHST = ${:,.2F}\nFinal Cost = ${:,.2F}".format(cost1_without_HST, HST_difference, cost1_with_HST)
		
		elif int(view['#_of_toppings_textfield'].text) == 1:
			cost2_without_HST = (EXTRA_LARGE_PIZZA + TOPPING_1)	
			cost2_with_HST = (EXTRA_LARGE_PIZZA + TOPPING_1) * HST
			HST_difference = cost2_with_HST - cost2_without_HST
			view['final_costs_label'].text = "Sub Total = ${:,.2F}\nHST = ${:,.2F}\nFinal Cost = ${:,.2F}".format(cost2_without_HST, HST_difference, cost2_with_HST)
		
		elif int(view['#_of_toppings_textfield'].text) == 2:
			cost3_without_HST = (EXTRA_LARGE_PIZZA + TOPPING_2)
			cost3_with_HST = (EXTRA_LARGE_PIZZA + TOPPING_2) * HST
			HST_difference = cost3_with_HST - cost3_without_HST
			view['final_costs_label'].text = "Sub Total = ${:,.2F}\nHST = ${:,.2F}\nFinal Cost = ${:,.2F}".format(cost3_without_HST, HST_difference, cost3_with_HST)
			
		elif int(view['#_of_toppings_textfield'].text) == 3:
			cost4_without_HST = (EXTRA_LARGE_PIZZA + TOPPING_3) 
			cost4_with_HST = (EXTRA_LARGE_PIZZA + TOPPING_3) * HST 
			HST_difference = cost4_with_HST - cost4_without_HST
			view['final_costs_label'].text = "Sub Total = ${:,.2F}\nHST = ${:,.2F}\nFinal Cost = ${:,.2F}".format(cost4_without_HST, HST_difference, cost4_with_HST)
		
		elif int(view['#_of_toppings_textfield'].text) == 4:
			cost5_without_HST = (EXTRA_LARGE_PIZZA + TOPPING_4)
			cost5_with_HST = (EXTRA_LARGE_PIZZA + TOPPING_4) * HST
			HST_difference = cost5_with_HST - cost5_without_HST
			view['final_costs_label'].text = "Sub Total = ${:,.2F}\nHST = ${:,.2F}\nFinal Cost = ${:,.2F}".format(cost5_without_HST, HST_difference, cost5_with_HST)

view = ui.load_view()
view.present('sheet')

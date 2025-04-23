import random

def generate_tickets(ticket_count, max_number) :
    result_list = random.sample([i for i in range(max_number)], ticket_count)
    return result_list, random.choice(result_list)

print(generate_tickets(5, 10))

'''
Solution by PCAP
import random
 
def generate_tickets(ticket_count, max_number):
    list_to_return = random.sample(range(0, max_number), ticket_count)
    return (list_to_return, random.sample(list_to_return, 1)[0])
'''

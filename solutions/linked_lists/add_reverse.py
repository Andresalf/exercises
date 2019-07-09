'''
Problem: Add two numbers whose digits are stored in a linked list in reverse order.
'''
from data_types.linked_list import Node, LinkedList


class MyLinkedList(LinkedList):

    def add_reverse(self, first_list, second_list):
        if not first_list or not isinstance(first_list, LinkedList):
            if not second_list or not isinstance(first_list, LinkedList):
                return None
            else:
                return second_list
        else:
            if not second_list or not isinstance(first_list, LinkedList):
                return first_list
            else:
                head1 = first_list.head
                head2 = second_list.head
                result = LinkedList()
                carry_on = 0
                while head1 or head2:
                    sum = (head1.data if head1 else 0) + (head2.data if head2 else 0) + carry_on
                    value = sum % 10
                    carry_on = sum // 10
                    result.append(value)
                    head1 = head1.next if head1 else None
                    head2 = head2.next if head2 else None
                
                if carry_on:
                    result.append(carry_on)
                    
                return result

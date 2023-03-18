/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun removeNthFromEnd(head: ListNode?, n: Int): ListNode? {
        
        val temp:ListNode = ListNode(0)
        temp.next = head
        
        var fast : ListNode =  temp
        var slow : ListNode = temp
        
        repeat(n){
            if(fast.next != null){
                fast = fast.next
            }
            else{
                return head
            }
        }
        
        while(fast.next != null){
            slow = slow.next
            fast = fast.next
        }
        slow.next = slow.next.next
        
        return temp.next
    }
}
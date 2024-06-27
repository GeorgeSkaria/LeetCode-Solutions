 
 #include <stdlib.h>
  *struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * }; 
 * 
 * 
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* cur = dummy;
    int carry = 0;
    
    while (l1 != NULL || l2 != NULL || carry != 0) {
        int val1 = 0;
        int val2 = 0;
        
        if (l1 != NULL) {
            val1 = l1->val;
            l1 = l1->next;
        }
        
        if (l2 != NULL) {
            val2 = l2->val;
            l2 = l2->next;
        }
        
        int total = val1 + val2 + carry;
        carry = total / 10;
        
        struct ListNode* new_node = (struct ListNode*)malloc(sizeof(struct ListNode));
        new_node->val = total % 10;
        new_node->next = NULL;
        
        cur->next = new_node;
        cur = new_node;
    }
    
    struct ListNode* result = dummy->next;
    free(dummy);  // Free the dummy node
    
    return result;
}
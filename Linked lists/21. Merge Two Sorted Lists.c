*
 * 
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 *
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    if (list1 == NULL)
        return list2;
    if (list2 == NULL)
        return list1;

    struct ListNode* head;
    struct ListNode* ptr;

    if (list1->val > list2->val) {
        head = list2;
        list2 = list2->next;
    } else {
        head = list1;
        list1 = list1->next;
    }

    ptr = head;

    while (list1 && list2) {
        if (list1->val > list2->val) {
            ptr->next = list2;
            list2 = list2->next;
        } else {
            ptr->next = list1;
            list1 = list1->next;
        }
        ptr = ptr->next;
    }

    if (!list1)
        ptr->next = list2;
    else
        ptr->next = list1;

    return head;
}

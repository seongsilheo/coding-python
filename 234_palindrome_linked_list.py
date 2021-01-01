# Deque : 삽입 및 삭제가 리스트의 양쪽 끝에서 모두 가능한 구조 사용
#
#
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = collections.deque()
        
        while head is not None:  # ListNode -> Deque
            q.append(head.val)
            head = head.next
            
        while len(q) > 1:
            if q.popleft() != q.pop(): # 양쪽에서 뺀값들 비교
                return False
            
        return True

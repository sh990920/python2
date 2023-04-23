'''
연결 리스트(Linked List)
  저장된 각 데이터가 (데이터)+(다음 데이터의 포인터)로 이루어진 것으로
  한 방향으로만 탐색 가능한 구조
'''
class Node:
  def __init__(self, data, next=None):
    self.data = data  # 노드에 저장될 데이터
    self.next = next  # 다음 노드를 가리키는 포인터

class LinkedList:
  def __init__(self):
    self.head = None # 머리 노드를 저장하는 멤버 변수
    
  def add_node(self, data):
    new_node = Node(data) # 새로운 노드 생성
    '''
    [7, 3노드 주소값] -> [3, 9노드 주소값] -> [9, None]
    '''
    if self.head is None: # 연결 리스트가 비어 있는 경우
      self.head = new_node
      return
    
    current = self.head
    while current.next is not None: # 연결 리스트의 끝까지 이동
      current = current.next
    
    current.next = new_node # 새로운 노드를 연결 리스트의 끝에 추가
    
  def insert_node(self, find_data, insert_data):
    
    if self.head is None: # 연결 리스트가 비어 있는 경우
      return
    '''
    7, 3, 9, 1, 6, 
    '''
    if self.head.data == find_data: # 머리 노드를 찾는 경우
      self.head = Node(insert_data, self.head)
      return
    
    current = self.head
    while current.next is not None: # 연결 리스트를 따라가면 원하는 노드 찾기
      if current.next.data == find_data:
        new_node = Node(insert_data, current.next)
        current.next = new_node
        return
      current = current.next
    
    # 원하는 노드를 찾지 못한 경우, 연결 리스트의 끝에 새로운 노드 추가
    self.add_node(insert_data)
    
      
  def delete_node(self, del_data):
    if self.head is None: # 연결 리스트가 비어 있는 경우
      return
    
    if self.head.data == del_data: # 머리 노드를 삭제하는 경우
      self.head = self.head.next
      return
    
    current = self.head
    while current.next is not None: # 연결 리스트를 따라가며 원하는 노드 찾기
      if current.next.data == del_data:
        current.next = current.next.next
        return
      current = current.next
      
  
  def print_list(self):
    current = self.head
    while current is not None: # 연결 리스트를 따라가며 데이터 출력
      print(current.data, end=' ')
      current = current.next

# 실행코드
linked_list = LinkedList()
linked_list.add_node(7)
linked_list.add_node(3)
linked_list.add_node(9)
linked_list.add_node(1)
linked_list.add_node(6)

linked_list.insert_node(9, 99) # 9 다음에 99삽입

linked_list.delete_node(1)

linked_list.print_list()


print('============================')

def changeData(node):
  node.data = 10

node1 = Node(5)

changeData(node1)
print(node1.data)
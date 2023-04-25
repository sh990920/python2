'''
파일명 : Ex06-BinaryTree.py

트리 자료구조
  단 하나의 루투 노드가 있고, 루트 노드에서 하위 노드들이 연결된
  비선형 계층구조이다.

이진트리(Binary Tree)
  모든 노드가 최대 2개의 자식 노드를 가질 수 있는 구조를 말한다.
  왼쪽 서브 트리의 값은 루트의 값보다 작고, 오른쪽 서브트리의 값은 루트보다 
  큰 값을 가지도록 구성한다.
'''

# 이진 트리의 각 노드를 정의하는 클래스
class TreeNode:
    def __init__(self, value):  # 생성자
        self.value = value  # 노드의 값
        self.left = None    # 왼쪽 서브트리 노드
        self.right = None   # 오른쪽 서브트리 노드

# 이진 트리를 생성하고 순회, 탐색, 삽입 삭제 하는 클래스
class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)  # 루트노드

    '''
    전위순회 left -> root -> right
    bt.preorder_traversal(bt.root, "")
    bt.preorder_traversal((5), "") -> traversal = 5# 
                (5) 1번 재귀
                -> preorder_traversal((3), "5#") -> traversal = 5#3#
                    (3) 1번 재귀
                    -> preorder_traversal((2), "5#3#") -> traversal = 5#3#2#
                        (2) 1번 재귀
                        -> preorder_traversal(None, "5#3#2#") -> traversal = 5#3#2#
                        (2) 2번 재귀
                        -> preorder_traversal(None, "5#3#2#") -> traversal = 5#3#2#
                    (3) 2번 재귀
                    -> preorder_traversal((4), "5#3#2#") -> traversal = 5#3#2#4#
                        (4) 1번 재귀
                        -> preorder_traversal(None, "5#3#2#4#") -> traversal = 5#3#2#4#
                        (4) 2번 재귀
                        -> preorder_traversal(None, "5#3#2#4#") -> traversal = 5#3#2#4#
                (5) 2번 재귀
                -> preorder_traversal((7), "5#3#2#4#") -> traversal = 5#3#2#4#7#
                    (7) 1번 재귀
                    -> preorder_traversal((6), "5#3#2#4#7#") -> traversal = 5#3#2#4#7#6#
                        (6) 1번 재귀
                        -> preorder_traversal(None, "5#3#2#4#7#6#") -> traversal = 5#3#2#4#7#6#
                        (6) 2번 재귀
                        -> preorder_traversal(None, "5#3#2#4#7#6#") -> traversal = 5#3#2#4#7#6#
                    (7) 2번 재귀
                    -> preorder_traversal((8), "5#3#2#4#7#") -> traversal = 5#3#2#4#7#6#8#
                        (8) 1번 재귀
                        -> preorder_traversal(None, "5#3#2#4#7#6#8#") -> traversal = 5#3#2#4#7#6#8#
                        (8) 2번 재귀
                        -> preorder_traversal(None, "5#3#2#4#7#6#8#") -> traversal = 5#3#2#4#7#6#8#
    '''
    
    def preorder_traversal(self, start, traversal):
        if start:
            traversal += (str(start.value) + '#')
            # 1번 재귀
            traversal = self.preorder_traversal(start.left, traversal)
            # 2번 재귀
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal
    
    '''
    print("중위 순회: ", bt.inorder_traversal(bt.root, ""))
    bt.inorder_traversal(bt.root, "")
    
    bt.inorder_traversal((5), "") -> traversal =  ""
        (5) 1번재귀
        ->bt.inorder_traversal((3), "") -> traversal =  ""
            (3) 1번 재귀
            ->bt.inorder_traversal((2), "") -> traversal =  ""
                (2) 1번 재귀
                ->bt.inorder_traversal(None, "") -> traversal =  ""
                (2) 중간코드 
                -> traversal +=  "2#" -> traversal =  2#
                (2) 2번 재귀
                ->bt.inorder_traversal(None, "2#") -> traversal =  2#
            (3) 중간코드
            -> traversal += 3# -> traversal =  2#3#
            (3) 2번 재귀
            ->bt.inorder_traversal((4), "2#3#") -> traversal =  "2#3#"
                (4) 1번 재귀
                ->bt.inorder_traversal(None, "2#3#") -> traversal =  "2#3#"
                (4) 중간코드
                -> traversal += 4# -> traversal =  2#3#4#
                (4) 2번 재귀
                ->bt.inorder_traversal(None, "2#3#4#") -> traversal =  "2#3#4#"
        (5) 중간코드
             -> traversal += 5# -> traversal =  2#3#4#5#
        (5) 2번 재귀
             ->bt.inorder_traversal((7), "2#3#4#5#") -> traversal =  "2#3#4#5#"
                (7) 1번 재귀
                -> bt.inorder_traversal((6), "2#3#4#5#") -> traversal =  "2#3#4#5#"
                    (6) 1번 재귀
                    -> bt.inorder_traversal(None, "2#3#4#5#") -> traversal =  "2#3#4#5#"
                    (6) 중간코드
                    -> traversal += 6# -> traversal =  2#3#4#5#6#
                    (6) 2번 재귀
                    -> bt.inorder_traversal(None, "2#3#4#5#6#") -> traversal =  "2#3#4#5#6#"
                (7) 중간코드
                -> traversal += 7# -> traversal =  2#3#4#5#6#7#
                (7) 2번 재귀
                -> bt.inorder_traversal((8), "2#3#4#5#6#7#") -> traversal =  "2#3#4#5#6#7#"
                    (8) 1번 재귀
                    -> bt.inorder_traversal(None, "2#3#4#5#6#7#") -> traversal =  "2#3#4#5#6#7#"
                    (8) 중간코드
                    -> traversal += 8# -> traversal =  2#3#4#5#6#7#8#
                    (8) 2번 재귀
                    -> bt.inorder_traversal(None, "2#3#4#5#6#7#8#") -> traversal =  "2#3#4#5#6#7#8#"
    '''
    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + '#')
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    
    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + ' ')
        return traversal
    

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, current_node):
        if not current_node:
            return False
        elif current_node.value == value:
            return True
        elif value < current_node.value:
            return self._search(value, current_node.left)
        else:
            return self._search(value, current_node.right)

    '''
    self.root = 5
    
    insert(3) -> _insert(3, TreeNode(5)) 
    '''
    # 삽입 메소드 : 이진 탐색을 사용하여 새 노드를 삽입
    def insert(self, value):
        # 이진 트리에 루트노드가 없는 경우 새 노드를  루트노드로 설정
        if not self.root:
            self.root = TreeNode(value)
        # 루트 노드가 있는 경우 _insert 메소드 호출하여 사입 수행
        else:
            self._insert(value, self.root)
    '''
    self.root = 5
    
    bt.insert(3) -> _insert(3, TreeNode(5)) -> TreeNode(5).left = TreeNode(3)
    bt.insert(7) -> _insert(7, TreeNode(5)) -> TreeNode(5).right = TreeNode(7)
    bt.insert(2) -> _insert(2, TreeNode(5)) -> _insert(2, TreeNode(3)) 
                                                = TreeNode(3).left = TreeNode(2)
    bt.insert(4) -> _insert(4, TreeNode(5)) -> _insert(4, TreeNode(3))
                                                = TreeNode(3).right = TreeNode(4)
    bt.insert(6) -> _insert(6, TreeNode(5)) -> _insert(6, TreeNode(7))
                                                = TreeNode(7).left = TreeNode(6)
    bt.insert(8) -> _insert(8, TreeNode(5)) -> _insert(8, TreeNode(7))
                                                = TreeNode(7).right = TreeNode(8)
    '''
    def _insert(self, value, current_node):
        
        if value < current_node.value:
           
            if not current_node.left:
                current_node.left = TreeNode(value)
            else:
                self._insert(value, current_node.left)
                
        elif value > current_node.value:
            
            if not current_node.right:
                current_node.right = TreeNode(value)
            else:
                self._insert(value, current_node.right)
                
        else:
            print("이미 존재하는 값입니다.")

    def delete(self, value):
        if not self.root:
            return
        else:
            self.root = self._delete(value, self.root)

    def _delete(self, value, current_node):
        if not current_node:
            return current_node

        elif value < current_node.value:
            current_node.left = self._delete(value, current_node.left)

        elif value > current_node.value:
            current_node.right = self._delete(value, current_node.right)

        else:
            if not current_node.left and not current_node.right:
                current_node = None

            elif not current_node.left:
                current_node = current_node.right

            elif not current_node.right:
                current_node = current_node.left

            else:
                min_node = self._find_min(current_node.right)
                current_node.value = min_node.value
                current_node.right = self._delete(min_node.value, current_node.right)

        return current_node

    def _find_min(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node


# 실행코드
# 이진 트리 객체를 생성합니다. 루트 노드의 값은 5입니다.
bt = BinaryTree(5)

# 값을 삽입합니다.
bt.insert(3)
bt.insert(7)
bt.insert(2)
bt.insert(4)
bt.insert(6)
bt.insert(8)

# 이진 트리를 전위 순회한 결과를 출력합니다.
print("전위 순회: ", bt.preorder_traversal(bt.root, ""))

# 이진 트리를 중위 순회한 결과를 출력합니다.
print("중위 순회: ", bt.inorder_traversal(bt.root, ""))

# 이진 트리를 후위 순회한 결과를 출력합니다.
print("후위 순회: ", bt.postorder_traversal(bt.root, ""))

# 값을 검색합니다.
print("값 4가 트리에 존재하는가? ", bt.search(4))
print("값 9가 트리에 존재하는가? ", bt.search(9))

# 값을 삭제합니다.
bt.delete(3)
print("값 3을 삭제한 후 중위 순회: ", bt.inorder_traversal(bt.root, ""))

# 값을 삭제합니다.
bt.delete(7)
print("값 7을 삭제한 후 중위 순회: ", bt.inorder_traversal(bt.root, ""))

# 값을 삭제합니다.
bt.delete(5)
print("값 5을 삭제한 후 중위 순회: ", bt.inorder_traversal(bt.root, ""))



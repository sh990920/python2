'''
해시테이블(Hash Table)
  해시 테이블(Hash Table)은 키와 값을 저장하는 데이터 구조로,
  요소의 빠르고 효율적인 검색, 삽입, 삭제를 허용한다.
  해시 함수는 키를 입력으로 받아 값을 저장하거나 검색할 수 있는
  배열 인덱스를 반환한다.
'''

class HashTable:
  def __init__(self, size):
    self.size = size # 해시 테이블의 크기
    self.hash_table = [None] * self.size
    
  def hash_function(self, key):
    # 해시 함수: key의 해시값을 계산한 후 해시 테이블의 크기로 나눈 나머지 반환
    return hash(key) % self.size
  
  def insert(self, key, value):
    hash_index = self.hash_function(key) # key의 해시값으로 해시 인덱스 계산
    
    if self.hash_table[hash_index] is None: # 해당 인덱스가 None이면 빈리시트 생성
      self.hash_table[hash_index] = []
    self.hash_table[hash_index].append((key, value))  #(key, value) 쌍 추가
  
  def search(self, key):
    '''
    John Doe
    '''
    hash_index = self.hash_function(key)
    bucket = self.hash_table[hash_index]
    if bucket is None:
      return None
    for k, v in bucket:
      if k == key:
        return v
    return None
    
    
# 실행 코드
hash_table = HashTable(10) # 크기가 10인 해시 테이블 생성
hash_table.insert('John Doe', '555-555-5555')
hash_table.insert('Jane Doe', '555-555-5556')
hash_table.insert('Jim Doe', '555-555-5557')
hash_table.insert('KoreaIT', '555-555-5558')

print(hash_table.search('John Doe'))
print(hash_table.search('Jane Doe'))
print(hash_table.search('Jim Doe'))
print(hash_table.search('KoreaIT'))
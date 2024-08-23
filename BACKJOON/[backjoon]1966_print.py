from collections import deque
t = int(input()) # 테스트케이스 수

for _ in range(t):
    n, m = map(int, input().split()) # 문서의 수, 궁금한 책이 현재 있는 위치
    query_book = m+1 # 궁금한 책의 번호
    
    deq = deque()
    imp_list = list(map(int, input().split())) # 중요도를 리스트로 저장
     
    for i in range(n):
        deq.append([i+1, imp_list[i]]) # deque에 책 번호와 중요도 순서대로 저장
        
    answer = [] # 인쇄 문서번호를 순서대로 저장
    
    while deq:
        book_n, book_i = deq.popleft()

        if any(book_i<x[1] for x in deq): # deq에 남아 있는 책들 중 중요도가 하나라도 높은게 있다면
            deq.append([book_n, book_i]) # 다시 deq에 append
        else:
            answer.append(book_n) # 현재 인쇄 대기문서가 가장 큰 우선순위라면, 인쇄 진행
            if book_n == query_book: # 이때 문서번호가 궁금한 책의 번호와 일치한다면
                print(answer.index(book_n) + 1) # 해당 문서의 인덱스(순서)에 1 더해 출력
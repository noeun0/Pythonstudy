#!/usr/bin/env python
# coding: utf-8

# 
# # 12. 기둥과 보 설치
# 
# 
# 컨셉
# 삽입
# - 2차원 리스트로 값을 입력받고, 첫반째 속성의 값을 각각 [x,y,a,b]라고 한다.
# - 보와 기둥의 값을 저장할 모든 값이 0인 리스트 하나 만들기.
#     b가 1인 경우 (삽입)
#         a가 0인 경우 기둥 (수직 1씩 증가).  -> (x,y)에 +1 , (x,y+1)에 +1
#         a가 1인 경우 보 (평행 1씩 증가).  -> (x,y)에 +1 , (x+1,y)에 +1
#     b가 0인 경우 (삭제)
#         a가 0인 경우 기둥 - (x,y)가 1이고 (x,y+1)가 3이면 각각에 -1
#         a가 1인 경우 보 - (x,y)가 1이고 (x+1,y)가 3이면 각각에 -1
# 
# 출력
# - 2차원 리스트에서, 0이 아닌 수를 찾으면
#     - (x,y+1) == 2이면 (x,y,0)를 result에 어펜드
#     - (x+1,y) == 2이면 (x,y,1)를 result에 어펜드
# - 정렬
# 
# 

# In[59]:


import copy

print ([0]*10)


# In[64]:


def solution(n, build_frame):
    list1=[]
    for _ in range(n+2):
        
        a = ([0]*(n+2))
        list1.append(copy.deepcopy(a))
        
    result = []
   # print (list1)
    for i in (build_frame):
        #print(i[2])
        
        if i[3]==1: 
            if i[2]==1:
                list1[i[0]][i[1]]+=1
                list1[(i[0])+1][i[1]] +=1
                #print(f"보삽입{list1}")
            if i[2]==0:
                list1[i[0]][i[1]] +=1
                list1[i[0]][i[1]+1] +=1
                #print(f"기둥삽입{list1}")
        elif i[3]==0: 
            if i[2]==1 and list1[i[0]][i[1]] ==1 and list1[i[0]+1][i[1]]==3: # 보삭제
                list1[i[0]][i[1]]-=1
                list1[i[0]+1][i[1]]-=1
            if i[3]==0 and list1[i[0]][i[1]] ==1 and list1[i[0]][i[1]+1]==3: # 기둥삭제
                list1[i[0]][i[1]]-=1
                list1[i[0]][i[1]+1]-=1
                
    for i in range(n+1):
        print(i)
        for j in range(n):
            if list1[i][j] !=0:
                if list1[i][j+1] >=2:
                    result.append([i,j,0])
                if list1[i+1][j] >=2:
                    result.append([i,j,1])
                    
                    
    print (result)         
            
                
    
    
    
solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])        


# In[44]:





# In[ ]:


m = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]


a = sorted(m)
print(a)


# In[ ]:





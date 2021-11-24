knap_sac_capacity=int(input('Enter Knapsak capacity: '))
weights=[]
profits=[]
profits.append(0)
weights.append(0)
we=[int(i) for i in input('Enter the weights: ').split(' ')]
for i in we:
    weights.append(i)
pr=[int(i) for i in input('Enter the Profits: ').split(' ')]
for i in pr:
    profits.append(i)
        
matrix=[]    
for i in range(len(weights)):
    matr=[]
    for j in range(knap_sac_capacity+1):
        matr.append(0)
    matrix.append(matr)

if(knap_sac_capacity>=weights[0]):
  
    for i in range(len(weights)):
        w=weights[i]
        for j in range(knap_sac_capacity+1):
            if i == 0 or j == 0 :
                matrix[i][j]=0
            elif(j<w):
              matrix[i][j]=matrix[i-1][j]
            else:
              matrix[i][j]=max(matrix[i-1][j], profits[i]+matrix[i-1][j-w])
        
print('\n')
for i in matrix:
    print(*i)

row=len(matrix)-1
column=knap_sac_capacity

list_weights=[]
while(row>-1 and column>-1):

  if(row==0 and column-weights[row]==0):
    list_weights.append(weights[row])
    break
  elif(column==0):

    break
  elif(matrix[row][column]==matrix[row-1][column]):
    row=row-1
  else:
    list_weights.append(weights[row])
    column=column-weights[row]

list_weights.sort()
for i in range(len(list_weights)):
    list_weights[i]=list_weights[i]-1
print("\nThere items selected will be:",*list_weights)

to=0
for i in list_weights:
    to+=profits[i]
    
    
print(f'Therefore Total Profit will be:{to}')

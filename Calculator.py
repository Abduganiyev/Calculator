# №1 Calculator
def add(data):
    sum=list(map(float,data.split('+')))
    sum=sum[0]+sum[1]
    if sum//10==0:
        sum=int(sum)
    print(sum)
def sub(data):
    sum=list(map(float,data.split('-')))
    sum=sum[0]-sum[1]
    if sum//10==0:
        sum=int(sum)
    print(sum)
def multiply(data):
    sum=list(map(float,data.split('*')))
    sum=sum[0]*sum[1]
    if sum//10==0:
        sum=int(sum)
    print(sum)
def div(data):
    sum=list(map(float,data.split('/')))
    sum=sum[0]/sum[1]
    if sum//10==0:
        sum=int(sum)
    print(sum)
def main(data):
    for i in data:
        if i=="+":
            add(data)
        elif i=="-":
            sub(data)
        elif i=="*":
            multiply(data)
        elif i=="/":
            div(data)
         
main(input())
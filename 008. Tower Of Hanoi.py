def toh(n, t1, t2, t3):
    if(n==0):
        return;
    toh(n-1,t1,t3,t2);
    print("{}{}{}{}{}{}".format(n,"[",t1," -> ",t2,"]"));
    toh(n-1,t3,t2,t1);



n = int(input())
n1,n2,n3 = int(input()),int(input()),int(input())
toh(n, n1, n2, n3);

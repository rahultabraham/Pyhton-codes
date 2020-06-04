
def dist_from_origin(x,y):
    return ((x**2+y**2)**(1/2))
def sort_array(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if(array[i]>array[j]):
                temp=array[i]
                array[i]=array[j]
                array[j]=temp
    return array

def findKClosestPoints(lst,k):
    dis=[]
    dic_of_dis={}
    points=[]
    for i in lst:
        a,b=i
        d_from_origin=dist_from_origin(a,b)
        dis.append(d_from_origin)
        dic_of_dis[d_from_origin]=a,b
    sorted_dis_list=sort_array(dis)
    for i in range(k):
        key=sorted_dis_list[i]
        points.append(dic_of_dis[key])
    return points
print(findKClosestPoints([(0,0),(2,3),(3,4),(-2,5),(1,4),(-1,1),(3,7),(-8,-3)],3))
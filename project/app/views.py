from django.shortcuts import render

# Create your views here.
def set(request):
    my_list1={'id':1,'name':'jyoti','city':'bhopal'}
    my_list2={'id':2,'name':'viti','city':'bhopal'}
    my_list=[my_list1,my_list2]
    request.session['data']=my_list

    # request.session['name']='jyoti'
    # request.session['city']='bhopal'
    # request.session['roll']=105

    return render(request,'set.html')

#minimum time for cookies are closing till browser,and for session is 14 days

def get(request):
    data1=request.session.get('data','Guest')
    return render (request,'get.html',{"name":data1})

def delete(request):
    # if 'data' in request.session:
    #     del request.session['data']
    
    request.session.flush()   #multiple oobject delete
    return render (request,'delete.html')
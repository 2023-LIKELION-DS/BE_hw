from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def wordCount(request):
    return render(request, "wordCount.html")

def result(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()
    
    word_dictionary = {}
    
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
            
    total_sum = sum(list(word_dictionary.values()))
            
    return render(request, "result.html", {'alltext': entered_text, 'dictionary': word_dictionary.items(), 'total': total_sum})
# 여기까지 하고 페이지 접속할 때 wordCount 통해서 글씨 입력하고 result 페이지로 넘어감, 바로 8000/result 하면 안됨

def hello(request):
    user = request.GET['username']
    return render(request, "hello.html", {'name' : user})
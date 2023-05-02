from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html')

def wordCount(request):
  return render(request, 'wordCount.html')

def result(request):
  entered_text = request.GET['fulltext']
  word_list = entered_text.split()
  word_directory = {}
  
  for word in word_list:
    if word in word_directory:
      word_directory[word] += 1
    else:
      word_directory[word] = 1
      
  word_length = len(word_list)
      
  context = {
    'alltext':entered_text, 
    'dictionary':word_directory.items(),
    'word_length':word_length,
  }
  return render(request, 'result.html', context=context)

def hello(request):
  name = request.GET['name']
  context = {
    'name':name, 
  }
  return render(request, 'hello.html', context=context)

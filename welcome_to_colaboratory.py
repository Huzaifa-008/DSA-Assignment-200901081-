# -*- coding: utf-8 -*-
"""Welcome to Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb

<p><img alt="Colaboratory logo" height="45px" src="/img/colab_favicon.ico" align="left" hspace="10px" vspace="0px"></p>

<h1>What is Colaboratory?</h1>

Colaboratory, or 'Colab' for short, allows you to write and execute Python in your browser, with 
- Zero configuration required
- Free access to GPUs
- Easy sharing

Whether you're a <strong>student</strong>, a <strong>data scientist</strong> or an <strong>AI researcher</strong>, Colab can make your work easier. Watch <a href="https://www.youtube.com/watch?v=inN8seMm7UI">Introduction to Colab</a> to find out more, or just get started below!

## <strong>Getting started</strong>

The document that you are reading is not a static web page, but an interactive environment called a <strong>Colab notebook</strong> that lets you write and execute code.

For example, here is a <strong>code cell</strong> with a short Python script that computes a value, stores it in a variable and prints the result:
"""

seconds_in_a_day = 24 * 60 * 60
seconds_in_a_day

"""To execute the code in the above cell, select it with a click and then either press the play button to the left of the code, or use the keyboard shortcut 'Command/Ctrl+Enter'. To edit the code, just click the cell and start editing.

Variables that you define in one cell can later be used in other cells:
"""

seconds_in_a_week = 7 * seconds_in_a_day
seconds_in_a_week

"""Colab notebooks allow you to combine <strong>executable code</strong> and <strong>rich text</strong> in a single document, along with <strong>images</strong>, <strong>HTML</strong>, <strong>LaTeX</strong> and more. When you create your own Colab notebooks, they are stored in your Google Drive account. You can easily share your Colab notebooks with co-workers or friends, allowing them to comment on your notebooks or even edit them. To find out more, see <a href="/notebooks/basic_features_overview.ipynb">Overview of Colab</a>. To create a new Colab notebook you can use the File menu above, or use the following link: <a href="http://colab.research.google.com#create=true">Create a new Colab notebook</a>.

Colab notebooks are Jupyter notebooks that are hosted by Colab. To find out more about the Jupyter project, see <a href="https://www.jupyter.org">jupyter.org</a>.

## Data science

With Colab you can harness the full power of popular Python libraries to analyse and visualise data. The code cell below uses <strong>numpy</strong> to generate some random data, and uses <strong>matplotlib</strong> to visualise it. To edit the code, just click the cell and start editing.
"""

import numpy as np
from matplotlib import pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()

"""You can import your own data into Colab notebooks from your Google Drive account, including from spreadsheets, as well as from GitHub and many other sources. To find out more about importing data, and how Colab can be used for data science, see the links below under <a href="#working-with-data">Working with data</a>.

## Machine learning

With Colab you can import an image dataset, train an image classifier on it, and evaluate the model, all in just <a href="https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb">a few lines of code</a>. Colab notebooks execute code on Google's cloud servers, meaning you can leverage the power of Google hardware, including <a href="#using-accelerated-hardware">GPUs and TPUs</a>, regardless of the power of your machine. All you need is a browser.

Colab is used extensively in the machine learning community with applications including:
- Getting started with TensorFlow
- Developing and training neural networks
- Experimenting with TPUs
- Disseminating AI research
- Creating tutorials

To see sample Colab notebooks that demonstrate machine learning applications, see the <a href="#machine-learning-examples">machine learning examples</a> below.

## More resources

### Working with notebooks in Colab
- [Overview of Colaboratory](/notebooks/basic_features_overview.ipynb)
- [Guide to markdown](/notebooks/markdown_guide.ipynb)
- [Importing libraries and installing dependencies](/notebooks/snippets/importing_libraries.ipynb)
- [Saving and loading notebooks in GitHub](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)
- [Interactive forms](/notebooks/forms.ipynb)
- [Interactive widgets](/notebooks/widgets.ipynb)
- <img src="/img/new.png" height="20px" align="left" hspace="4px" alt="New"></img>
 [TensorFlow 2 in Colab](/notebooks/tensorflow_version.ipynb)

<a name="working-with-data"></a>
### Working with data
- [Loading data: Drive, Sheets and Google Cloud Storage](/notebooks/io.ipynb) 
- [Charts: visualising data](/notebooks/charts.ipynb)
- [Getting started with BigQuery](/notebooks/bigquery.ipynb)

### Machine learning crash course
These are a few of the notebooks from Google's online machine learning course. See the <a href="https://developers.google.com/machine-learning/crash-course/">full course website</a> for more.
- [Intro to Pandas DataFrame](https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/pandas_dataframe_ultraquick_tutorial.ipynb)
- [Linear regression with tf.keras using synthetic data](https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/linear_regression_with_synthetic_data.ipynb)


<a name="using-accelerated-hardware"></a>
### Using accelerated hardware
- [TensorFlow with GPUs](/notebooks/gpu.ipynb)
- [TensorFlow with TPUs](/notebooks/tpu.ipynb)

<a name="machine-learning-examples"></a>

## Machine learning examples

To see end-to-end examples of the interactive machine-learning analyses that Colaboratory makes possible, take a look at these tutorials using models from <a href="https://tfhub.dev">TensorFlow Hub</a>.

A few featured examples:

- <a href="https://tensorflow.org/hub/tutorials/tf2_image_retraining">Retraining an Image Classifier</a>: Build a Keras model on top of a pre-trained image classifier to distinguish flowers.
- <a href="https://tensorflow.org/hub/tutorials/tf2_text_classification">Text Classification</a>: Classify IMDB film reviews as either <em>positive</em> or <em>negative</em>.
- <a href="https://tensorflow.org/hub/tutorials/tf2_arbitrary_image_stylization">Style Transfer</a>: Use deep learning to transfer style between images.
- <a href="https://tensorflow.org/hub/tutorials/retrieval_with_tf_hub_universal_encoder_qa">Multilingual Universal Sentence Encoder Q&amp;A</a>: Use a machine-learning model to answer questions from the SQuAD dataset.
- <a href="https://tensorflow.org/hub/tutorials/tweening_conv3d">Video Interpolation</a>: Predict what happened in a video between the first and the last frame.
"""

#Assignment-1
#NAME: Huzaifa Ahamd//
#Reg NO#: 200901081//
#QNO.1//
class ArrayStack:
    """LIFO Stack implementatino using a Python list as underlying storage."""
    
    def __init__(self):
        self._data = []
        
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)
        
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
        
x = ArrayStack()
x.push(5)
x.push(3)
x.pop()
x.push(2)
x.push(8)
x.pop()
x.pop()
x.push(9)
x.push(1)
x.pop()
x.push(7)
x.push(6)
x.pop()
x.pop()
x.push(4)
x.pop()
x.pop()

#Q NO.2
x = ArrayStack()
class ArrayStack:
    """LIFO Stack implementatino using a Python list as underlying storage."""
    
    def __init__(self):
        self._data = []
        
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)
        
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            print("EMPTY WARNING")
            return
#             raise Empty('Stack is empty')
        return self._data.pop()
for i in range(7):
    x.push(i)
for i in range(10):
    x.pop()
for i in range(18):
    x.push(i)

#Q NO.3
class ArrayStack:
    """LIFO Stack implementatino using a Python list as underlying storage."""
    
    def __init__(self):
        self._data = []
    
    @property
    def data(self):
        return self._data
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)
        
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
    
    def transfer(self, S: ArrayStack) -> None:
        stck_len = len(self._data)
        [S.push(self.pop()) for _ in range(stck_len)]
    
x = ArrayStack()
for i in range(10):
    x.push(i)
x.data
y = ArrayStack()
x.transfer(y)
y.data

#Q NO.4
class ArrayStack:
    """LIFO Stack implementatino using a Python list as underlying storage."""
    
    def __init__(self):
        self._data = []
    
    @property
    def data(self):
        return self._data
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)
        
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
    
    def transfer(self, S: ArrayStack) -> None:
        stck_len = len(self._data)
        (S.push(self.pop()) for _ in range(stck_len))
    
    def pop_all(self):
        if self.data:
            self.pop()
            return self.pop_all()
x = ArrayStack()
for i in range(10):
    x.push(i)
x.data
x.pop_all()
x.data

#Q NO.5
"""
Note, this relies on the stack from R6-3
"""

def reverse_list(S):
  temp = Stack()
   for e in S:
        temp.push(e)
    
    for i in range(len(S)):
        S[i] = temp.pop()

lists = [[1,2,3,4,5,6],
        [3,2,5,6,7,8,9,5],
        [9,8,7,6,5,4,3,2,1]]

for l in lists:
    print ('Before: ', l)
    reverse_list(l)
    print('After:  ', l)
    print()

#Q NO.6

#------------R6-6---------------------
"""
Note, this relies on the Stack class form R6-3

"""

"""
Note 2: This is a sloppy implementation of this solution!


I'm not entirely sure what this problem is asking since the solution presented 
in Code Fragment 6.4 would work here as well.  Instead, I think it might be checking
that the order is (sequence that produces a num) operator (sequence that produces a num)

ex.. (5+4)*(3/(2+3)) is correct

The recursive aspect would involve checking that the values within a set of brackets is also an arithmetic expression,
with the base case being that you don't find any 



Add to stack until you get to a close bracket, then perform a 'check pop' until you get to the previous open bracket.
The result should be a number


An alternative approach using recursion is to focus more on the (sequence that produces a num) operator (sequence that produces a num)

Which means that you start by either finding a number or an (.  If you find an (, recurse to see if it collapses into 
a number.  If so, then look for an operation and the next number, and see if those collapse as well

Every time you see the num op num patterns you collapse into one number


"""



class AlgoStack(Stack):
    def __repr__(self):
        return str(self._data)
    
    
    OPEN, CLOSE, OPERATORS = '(', ')', '+-/*^'
    NUMBERS = '1234567890.'
    def pop_until_open(self):
        operator = True
        while not self.is_empty():
            ans = self.pop()
            if ans in self.OPERATORS:
                if operator: return False
                else: operator = True
                    
            elif ans in self.NUMBERS:
                operator = False
                
            elif ans in self.CLOSE: return False
            elif ans in self.OPEN: 
                self.push('3')
                return True  
            
        return False  #if you don't find an open bracket, there is a mismatch
    
    def check_expression(self, expression):
        for char in expression:
            
            if char in self.CLOSE:
                if not self.pop_until_open(): return False
            else: self.push(char)
        return True
    

    
exps = ['(5+4)*(3/(2+3))',
       '(5+4+)*(3/(2+3))',
        '(5+4))*(3/(2+3))',
       '5+(5+4)*(3/(2+3))']
for exp in exps:
    ss = AlgoStack()
    print(exp, ss.check_expression(exp))

#Q NO.7
class ArrayQueue:
    
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]
    
    def dequeue(self):
        
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front +1) % len(self._data)
        self._size -= 1
        
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer
    
    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
    
    def _resize(self, cap):
        
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
x = ArrayQueue()
x.enqueue(5)
x.enqueue(3)
x.dequeue()
x.enqueue(2)
x.enqueue(8)
x.dequeue()
x.dequeue()
x.enqueue(9)
x.enqueue(1)
x.dequeue()
x.enqueue(7)
x.enqueue(6)
x.dequeue()
x.dequeue()
x.enqueue(4)
x.dequeue()
x.dequeue()

"""#Q NO.8
22

Like before, a dequeue operation that fails doesn't remove anything from the queue, so there are essentially 10 dequeues

First operations don't change the queue at all

Therefore we have 32-10 = 22 (the size of the queue is 22 at that point)
"""

#Q NO.9
"""
Since it was initially an empty queue, we will assume the front value was initially 0 (althogh this is
not necessarily the case since you can empty the queue when front is a value other than 1)

self._front only increments when a dequeue takes place so the final value would be 10 ahead of its initial value, 
or self._front == 10 is self._front was initially 0 as assumed. More generally, it's (10+initial) % 30

"""

#Q NO.10
"""
This method will copy the data in exactly, but now there will be a huge gap between the middle of the data
filled with None and the next value (which is situated at ._data[0])

ex. a queue with 1,2,3,4,5,6,7 with front = 3:
      F
5,6,7,1,2,3,4

would become:
      F
5,6,7,1,2,3,4,N,N,N,N,N,N,N

the next insertion would be at front + self._size, which would be:
      F
5,6,7,1,2,3,4,N,N,N,8,N,N,N and so on, which results in the fragmentation of the data.  Successive dequeues would 
result in 1,2,3,4,N,N,N,....., N,N instead of the desired 1,2,3,4,5,6,7, is_empty==True


In contract, the walk assures that the data will stay both in order and in direct sequence, producing:

F
1,2,3,4,5,6,7,N,N,N,N,N,N,N

"""

#Q NO.11
"""
In our ADT, we want the following behaviours:

enqueue
dequeue
first
is_empty
len



"""


import collections

class Queue():
    def __init__(self):
        self._data = collections.deque()
        self._size = 0
        
        
    def __len__(self):
        return self._size
    
    def first(self):
        return self._data[0]
        
    def enqueue(self, value):
        self._size += 1
        self._data.append(value)  #Note we append here to add an element to the end of the queue
        
    def is_empty(self):
        return self._size == 0
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        else:
            ans = self._data.popleft()
            self._size -= 1
            return ans
        
        
dq = Queue()

for i in range(10):
    dq.enqueue(i)

    
print('First', dq.first(), 'Length', len(dq))
while not dq.is_empty():
    print( dq.dequeue(),  end = ', ')

#Q NO.12
"""

Return   Values in the Stack
-        [4]
-        [4, 8]
-        [4, 8, 9]
-        [5, 4, 8, 9]
9        [5, 4, 8, 9] (the back operation - I'm assuming they meant last() based on their implementation)
5        [4, 8, 9]
9        [4,8]
-        [4,8,7]
4        [4,8,7]
7        [4,8,7]
-        [4,8,7,6]
4        [8,7,6]
8        [7,6]

"""

#Q NO.13
#------------R6-13----------------
"""
D is a deque, which means that it can accept input at either end

Q is a queue, which follows the FIFO approach

Note, you can check whether each step is correct by commenting out the
subsequent lines and checking against output at that point

"""
import collections

#Setup
D = collections.deque()
Q = Queue()
for i in range(1, 9, 1):
    D.append(i)
    
    
def rearrange_using_queue(D, Q):    
    for i in range(5):             #   D          Q
        Q.enqueue(D.popleft())     #[6,7,8], [1,2,3,4,5]
        
    for i in range(3):
        D.append(Q.dequeue())      #[6,7,8,1,2,3], [4,5]
        
    
    for i in range(2):
        D.appendleft(Q.dequeue())  #[5,4,6,7,8,1,2,3], []
        
    for i in range(3):
        Q.enqueue(D.pop())         #[5,4,6,7,8], [3,2,1]
    
    for i in range(3):
        D.appendleft(Q.dequeue())  #[1,2,3,5,4,6,7,8]
    
    
rearrange_using_queue(D, Q)

print('Values of Q:')
while not Q.is_empty():
    print(Q.dequeue())
    
    
print('Values of D')
while len(D) != 0:
    print(D.popleft())

#Q NO.14
import collections

S = Stack()
D = collections.deque()

for i in range(1,9,1):
    D.append(i)
    

    
def rearrange_using_stack(D, S):
    for _ in range(4):
        S.push(D.popleft())    # [5,6,7,8], [1,2,3,4]
        
    D.append(S.pop())          # [5,6,7,8,4], [1,2,3]
    
    S.push(D.popleft())        # [6,7,8,4], [1,2,3,5]
    
    S.push(D.pop())            # [6,7,8], [1,2,3,5,4]
    
    for _ in range(5):
        D.appendleft(S.pop())  #[1,2,3,5,4,6,7,8], []
    
    
    
    
    
rearrange_using_stack(D, S) 
    
    
print('Values of S')
while not S.is_empty():
    print(S.pop())
    
print('Values of D:')
while len(D) != 0:
    print(D.popleft())
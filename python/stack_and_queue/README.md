# Stacks and Queues

Implementation Stack and Queue.
## Challenge
- [x]Can successfully push onto a stack.
- [x]Can successfully push multiple values onto a stack.
- [x]Can successfully pop off the stack.
- [x]Can successfully empty a stack after multiple pops.
- [x]Can successfully peek the next item on the stack.
- [x]Can successfully instantiate an empty stack.
- [x]Calling pop or peek on empty stack raises exception.
- [x]Can successfully enqueue into a queue.
- [x]Can successfully enqueue multiple values into a queue.
- [x]Can successfully dequeue out of a queue the expected value.
- [x]Can successfully peek into a queue, seeing the expected value.
- [x]Can successfully empty a queue after multiple dequeues.
- [x]Can successfully instantiate an empty queue.
- [x]Calling dequeue or peek on empty queue raises exception.

## Approach & Efficiency
Big O :
For the time => O(n)
For the space => O(1)

## API 
#### Stack
- Push method: adds a new node with that value to the top of the stack with an O(1) Time performance.
- Pop method: Removes the node from the top of the stack.
- Peek method:Returns: Value of the node located at the top of the stack.
- Is empty method: Returns: Boolean indicating whether or not the stack is empty.
#### Queue
- Enqueue method :adds a new node with that value to the back of the queue with an O(1) Time performance.
- Dequeue method: Removes the node from the front of the queue.
- Peek method:Returns: Value of the node located at the top of the stack.
- Is empty method: Returns: Boolean indicating whether or not the stack is empty.
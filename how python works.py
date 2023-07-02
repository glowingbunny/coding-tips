"""
- In a compiled language, the target machine directly translates the program. In an interpreted language, the source code is not directly
translated by the target machine. Instead, a different program, aka the interpreter, reads and executes the code

- Compiled languages are converted directly into machine code that the processor can execute. They tend to be faster and more efficient to
execute than interpreted languages. They also give the developer more control over hardware aspects, like memory management and CPU usage
- Compiled languages need a “build” step - they need to be manually compiled first. You need to "rebuild" the program every time you need to
make a change

- Interpreters run through a program line by line and execute each command (python is an Interpreted language)
- Python is actually translated to bytecode beforehand, so it can be read by the interpreter. Then the bytecode is translated to
machine code in live time through the interpreter
- This bytecode is a low-level set of instructions that can be executed by an interpreter. Instead of executing the instructions on CPU,
bytecode instructions are executed on a Virtual Machine
"""

import inspect

def func(x):
	return(x**2)
print(func(2))

print(inspect.getsource(func))  #getsource method: gets source code of func

from queue import Queue
print(inspect.getsource(Queue))  #we can see source code of imported modules

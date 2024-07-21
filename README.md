In this project, I learned about the following concepts:
Multitasking
Multitasking refers to the ability of an operating system to execute multiple tasks (processes) simultaneously. There are two primary types of multitasking:
Process-based Multitasking:
Involves running multiple processes (independent programs) at the same time.
Each process has its own memory space.
Process switching is managed by the operating system, which allocates CPU time to each process.
Thread-based Multitasking:
Involves running multiple threads within a single process.
Threads share the same memory space but run independently.
More efficient than process-based multitasking because it reduces the overhead of memory allocation.
Multithreading
Multithreading is a form of multitasking where a single process contains multiple threads executing concurrently.
Main Thread:
The initial thread that is created when a process starts.
Often responsible for managing other threads.
Creating Thread Methods:
Threads can be created using various methods provided by the programming language or threading library.
For example, in Python, threads can be created using the threading module.
Starting Threads:
Once a thread is created, it needs to be started to begin execution.
This is typically done by calling a start method.
Thread Management
Setting and Getting Thread Name:
Threads can be named to make them easier to identify.
Methods are available to set and get the names of threads.
Thread Synchronization
Thread synchronization is essential to prevent race conditions, which occur when multiple threads try to access shared resources simultaneously.
Methods for Synchronization:
Locks: Ensure that only one thread can access a resource at a time.
Semaphores: Allow a limited number of threads to access a resource.
Monitors: Combine locks and condition variables to manage thread access.
Thread Communication
Threads often need to communicate with each other to coordinate their actions.
Methods for Thread Communication:
Event Objects: Used for signaling between threads.
Condition Variables: Allow threads to wait for certain conditions to be met.
Queues: Provide a thread-safe way to exchange data between threads.
Daemon Threads
Daemon Threads:
Background threads that run continuously and perform tasks such as garbage collection.
Daemon threads are typically low-priority and are terminated when the main program exits.
These concepts form the foundation for understanding and implementing multitasking and multithreading in various programming projects.

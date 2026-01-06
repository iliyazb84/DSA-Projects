# Data Structures Implementation – Final Term Project

This repository contains my **final-term project** for the **Data Structures** course.
The goal of this project is to **implement different data structures from scratch**, **without using built-in data structure methods**, and to understand their internal working and behavior.

> 📌 **Important:** All data structures and required methods are implemented manually.
> ⭐ Parts marked as *bonus* in the project description are optional and give extra credit.

---

## 📂 Project Structure

Each data structure is implemented as a **separate project/module** and follows the specifications given in the course assignment.

---

## 🧩 Project 1: Recursive Functions

Implemented using **pure recursion**:

* Power function
  `F(a, b) → a^b`
* Combination function (nCr)
* Tower of Hanoi problem

---

## 🧮 Project 2: Arrays

* Sparse matrix generation from an `n × n` matrix
* Complete implementation of Array data structure

### Implemented Methods:

* `Insert(object, index)`
* `Delete(index) → object`
* `Find(object) → index`

---

## 🔁 Project 3: Queue

Queue implementations using **arrays**:

* Simple Queue
* Circular Queue

### Implemented Methods:

* `Enqueue(object)`
* `Dequeue() → object`
* `Peek() → object`
* `ReverseQueue() → queue`
* `IsEmpty() → boolean`
* `IsFull() → boolean`

---

## 📚 Project 4: Stack

* Queue implemented **only using Stack**
* Stack implementation from scratch

### Stack Methods:

* `Push(item)`
* `Pop() → item`
* `Peek() → item`
* `IsEmpty() → boolean`

---

## 🔗 Project 5: Linked List

Implemented different types of linked lists:

* Singly Linked List
* Circular Linked List
* Doubly Linked List

### Common Methods:

* `InsertAtBegin(data)`
* `InsertAtEnd(data)`
* `InsertAtIndex(data, index)`
* `UpdateNode(data, index)`
* `RemoveNodeAtBegin() → data`
* `RemoveNodeAtEnd() → data`
* `RemoveNodeAtIndex(index) → data`
* `SizeOfList() → size`
* `Concatenate(LinkedList)`
* `Invert()`

### Additional Implementations (using Linked List):

* Array using Linked List
* Queue using Linked List
* Stack using Linked List

> ⚠️ Note: These structures are implemented **only using the custom Linked List**, not built-in structures.

---

## 🌐 Project 6: Graph

Graph implementation with traversal algorithms:

### Implemented Methods:

* `AddVertex(vertex)`
* `AddEdge(firstVertex, secondVertex)`
* `RemoveEdge(firstVertex, secondVertex)`
* `RemoveVertex(vertex)`
* `BFS() → string`
* `DFS() → string`

---

## ⭐ Bonus Project: Hash Table

Custom implementation of a Hash Table:

### Implemented Methods:

* `HashFunction(key) → index`
* `Insert(key, value)`
* `Remove(key) → value`
* `Search(key) → value`

---

## 🛠️ Technologies

* Language: **Python**
* No built-in data structure methods were used for core logic

---

## 🎯 Purpose of the Project

* Deep understanding of data structures
* Learning how structures work internally
* Strengthening problem-solving skills

---

📌 *This repository is for educational purposes only.*

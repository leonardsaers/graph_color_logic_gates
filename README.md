# Theory

* https://www.youtube.com/watch?v=B5_m8lKULlI

* https://www.electronics-tutorials.ws/logic/universal-gates.html


# Prepare

pip install networkx matplotlib

# The 3-color graph OR gate

The following graph will act as an or gate if colored using only the three colors F,T and N. 

The node x1 or x2 will depend on note x1 and x2 according to the following truth table.

|x1|x2|x1 or x2|
|--|--|--------|
|F |F | F      |
|T |F | T      |
|F |T | T      |
|T |T | T      |

```

┌───┐   ┌───┬─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐   
│ F ├───┤ N ├ ─ ─ ─ ─┐                         
└─┬─┘   └─┬┬┘                               │   
  │       │          │                         
  │ ┌───┐ ││                                │   
  └─┤ T ├─┘          │                         
    └───┴──┼───────────────┬──┐             │   
              ┌──────┼─────┤  ├───────┐        
           │  │            └──┘       │     │   
              │      │                │        
           │  │    ┌───┐     ┌──┐     │     │   
              │ ┌──┤x1 ├─────┤  ├─┐   │        
           │┌─┴┬┘  └───┘     └┬─┘ └──┬┴─────┴──┐
            │  │              │      │x1 or x2 │
           │└──┴┐  ┌───┐     ┌┴─┐ ┌──┴─────────┘
                └──┤x2 ├─────┤  ├─┘             
           │       └───┘     └──┘               
            ─ ─ ─ ─ ┘                           
```

# The 3-color graph NOT gate

The NOT gate is easy to construct, just connect two nodes and you have a NOT gate, and connect the nodes to the N color.

That give the following truth table:

|x | NOT x |
|--|-------|
|F | T     |
|T | F     |


```
           ┌───┐   ┌───┐                                                               
           │ F ├───┤ N ├ ─ ─ ─ ─ ─ ┐                                                   
           └─┬─┘   └─┬─┴┐                                                              
             │ ┌───┐ │             │                                                   
             └─┤ T ├─┘  │                                                              
               └───┘               │                                                   
                        │                                                              
                                   │                                                   
                      ┌─┴─┐      ┌───────┐                                             
                      │ x ├──────┤ not x │                                             
                      └───┘      └───────┘ 
```

# 3-color graph logic gates

If you can construct an OR and a NOT gate, then you can construct any type of logic gate.

Most logic gates will be represented by a lot of nodes and edges but the number of nodes will still grow in O(n) where n is the number of logic gates.

# The 3-color graph problem

The challenge to color a graph and only using 3 color is np complete. A classical computer is not able to do that task in reasonable time.

A greedy algorithm can solve the graph coloring problem if a fourth color is introduced, but then the graph will not act as logic gates.

Any program could be programed using a 3 color graph since all locig gates can be represented within the graph.

# The challange

If there is a machine that can solve the 3 coloring graph problem, than code could be excecuted backwards.

The following graph would returne the input data that result in a false out from an OR gate.

```

┌───┐   ┌───┬─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐   
│ F ├───┤ N ├ ─ ─ ─ ─┐                         
└─┬─┘   └─┬┬┘                               │   
  │       │          │                         
  │ ┌───┐ ││                                │   
  └─┤ T ├─┘          │                         
    └┬──┴──┼───────────────┬──┐             │   
     │        ┌──────┼─────┤  ├───────┐        
     │     │  │            └──┘       │     │   
     │        │      │                │        
     │     │  │    ┌───┐     ┌──┐     │     │   
     │        │ ┌──┤x1 ├─────┤  ├─┐   │        
     │     │┌─┴┬┘  └───┘     └┬─┘ └──┬┴─────┴──┐
     │      │  │              │      │x1 or x2 │
     │     │└──┴┐  ┌───┐     ┌┴─┐ ┌──┴─────────┘
     │          └──┤x2 ├─────┤  ├─┘      │      
     │     │       └───┘     └──┘        │      
     │      ─ ─ ─ ─ ┘                    │
     │                                   │
     └───────────────────────────────────┘
```

The following code would create the above graph:

```python
GraphBuilder()
         .add_input("x1")
         .add_input("x2")
         .add_or("id1","x1","x2","x1_OR_x2")
         .add_edge("T","x1_OR_X2")
         .build()
```

More complex gates can be created. Here is the code for a half adder:

```python
GraphBuilder()
         .add_input("x1")
         .add_input("x2")
         .add_or("id1","x1","x2","carry")
         .add_xor("id2","x1","x2","sum")
         .build()
```

... any setup of logic gate could be represented by a 3-coloring graph.

If the magic machine that can solve a 3-coloring graph problem would provide a random sample of the input data that correspond to the output, than it would be possible (without using motecarlo) to retrieve the distribution of input data that results in a specific output.

Is it possible to reverse runs circuits using a machine that solves 3 coloring graph problem?


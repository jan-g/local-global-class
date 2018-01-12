# Quick example of turning data structures + functions into classes

This shows three approaches. The first is a very mathematical one, where
the data structres are managed separately from the functions that operate
on them.

The second approach is rather forced; rather than passing parameters between
function invocations, we use globals to store them. This approach *might*
be appropriate if you have one copy of global state, but taste around this
varies and it can produce some visceral reactions.

The final version shows how we've mechanically transformed the same functions
into methods on a class.

There's an added bonus that shows how multiple classes can implement the
same set of methods, which (when used appropriately) can lead to some expressive
gains.

The four files can be viewed in alphabetical order.

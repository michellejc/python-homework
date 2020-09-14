Strictly Increasing
--------

Given a sequence of numbers, check to see if the numbers are strictly increasing. In other words, is next number always greater than previous number?


All equal
-----

Check if all items in a list are equal.

Do __not__ change the type of the items in the list.




Duplicity problem
----

Remove duplicates while keeping order.

If an item appears multiple times, keep only the 1st occurrence. 

Do __not__ change the type of the items in the list.


Dropped data problem
----

You are doing data analysis work and realize something is wrong. There are two sequences of data - `old` and `new`. Items might be missing from `new`. Find the items appear in `old` but do not appear in `new`. Assume items can only be missing just from `new`.

Do __not__ change the type of the items in the list.

This is related to an important concept in distributed computing: [at-most-once delivery, at-least-once delivery, and exactly-once delivery](https://stackoverflow.com/questions/44204973/difference-between-exactly-once-and-at-least-once-guarantees)

Valid pairs
-----

Given a collection of matched pairs, determine if a string has valid ordering of matched pairs. 

Every opening element of a pair must be closed by the other element of the pair. Every open pair must be closed in the correct order. See unit tests for examples. 

Ignore all other characters.

This is a common interview problem. It attempts to asses your ability to effectively and efficiently process a stream of data.

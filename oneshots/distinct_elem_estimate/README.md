# Distinct Element Estimation

It's quite easy to count the number of elements in a very large set. Just keep one integer and increment for each element.
What if we only want the count of unique elements? This makes the problem much harder, we need to keep track of each previous unique element which typically entails hashsets. This works for small to medium sets, but for large sets the best we can do is a probabilistic estimate.

The typical state of the art for this is [HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog) which has lots of useful properties including unions, but we're going to use a much newer and more elegant algorithm, called [CVM](https://arxiv.org/abs/2301.10191) after its creators.

## CVM

The algorithm is based on flipping probability calculations on its head. Suppose you had a list of 40 elements, and you were told that the list was much larger but for each element you removed them with probability 0.5. Then you could estimate the list must have originally had around $n = 40 / 0.5 = 80$ elements. This is the core idea behind CVM.

The core of the algorithm is that you keep a set $S$ with max size $t$ (which is a parameter you can choose that affects the error bounds), and you keep a sampling rate $p$, which is initially 1.
Then you read off the elements of the stream and for each element, you first remove it from the set (if present), then you add it to the set with probability $p$.
Once the size of $S$ is $t$ then you throw away each element with probability $1/2$ and halve $p$.
After you've read all the elements you can estimate the number of distinct elements by reading off the size of $S$ and dividing by the sampling rate $\dfrac{|S|}{p}$.

## Tests

Let's do a small scale test on Hamlet by Shakespeare. With 30,557 words Hamlet sets the record as Shakespeare's longest play. We can use this as a test case for our algorithm.

Our version of Hamlet has 31,955 words

| t = 1000 | t = 5000 | actual |
| -------- | -------- | ------ |
| 7,984    | 7,820    | 7,806  |

What about the complete works of Shakespeare?

| t = 100 | t = 5000 | actual |
| ------- | -------- | ------ |
| 66,816  | 67,824   | 67,802 |

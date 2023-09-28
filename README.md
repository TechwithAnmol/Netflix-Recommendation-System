<h1>**What is the Multi-Armed Bandit Problem (MABP)?** \n
A bandit is defined as someone who steals your money. A one-armed bandit is a simple slot machine wherein you insert a coin into the machine, pull a lever, and get an immediate reward. But why is it called a bandit? It turns out all casinos configure these slot machines in such a way that all gamblers end up losing money!

A multi-armed bandit is a complicated slot machine wherein instead of 1, there are several levers which a gambler can pull, with each lever giving a different return. The probability distribution for the reward corresponding to each lever is different and is unknown to the gambler.

<h1>**Personalization at Netflix** \n
Within this domain Jaya Kawale and Fernando Amat (Netflix) shared two case studies: artwork optimization and billboard selection. The artwork optimization was earlier extensively described in at their techblog. The research on the billboard recommendation was new. Both aim to determine an incremental effect within an unknown reward distribution. This requires a multi-armed bandit solution as traditional machine learning can’t model this effect.
The basic aim of Artwork personalization is to display a variety of posters for the same show, which may be more appealing to the audience than the other ones.
There are a variety of algorithms to solve Multi-Armed Bandit problem:

Epsilon Greedy
Decayed Epsilon Greedy
UCB(Upper confidence Bound)
Softmax Exploration
Upper Confidence Bound (UCB) is the most widely used solution method for multi-armed bandit problems. This algorithm is based on the principle of optimism in the face of uncertainty.

In other words, the more uncertain we are about an arm, the more important it becomes to explore that arm.

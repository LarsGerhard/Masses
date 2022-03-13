#Masses Part 2

##Question 1


Although I can't think of how the system would need to be set up, you could theoretically set up the system where each spring pulls on its neighbours in such a way that their forces
cancel, except for one spring.

This makes sense with linear algebra because the eigenvectors form a basis, so you can make any complex wave that you want with a linear combination of eigenvectors

##Question 2

You can get only 3 masses moving through any symmetric initial conditions (i.e. x0 = [1,0,-1,0,1]. This physically makes sense because
Mass 1 and Mass 2 are pulled only by their two neighbours. So if those two neighbours pull an equal amount, then they won't move

This makes sense with linear algebra because the eigenvectors form a basis, so you can make any complex wave that you want with a linear combination of eigenvectors

##Question 3

I find that with eigenvalues all of the masses have a standard sin/cos wave rather than something more complex

##Question 4

The waves appear to almost share nodes (precision might be hurt by rounding). The vector I use is created in the included python script

##Question 5

Yep! You can recreate any complex waves with eigenvectors because they form a basis
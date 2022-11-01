
/* Relationships */
company(sumsum).
company(appy).
boss(stevey,appy).
developed(sumsum,galactica-s3).
smartphonetechnology(galactica-s3).
steal(stevey,galactica-s3).
competitors(sumsum, appy).

/* Rules */
competitors(X, Y):-
	competitors(Y, X).
business(X):- smartphonetechnology(X).
rival(X,Y):- competitors(X, Y), X\=Y.
unethical(X):- boss(A,B),steal(A,D), business(D), developed(C,D),rival(B,C),company(C).




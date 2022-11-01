/* facts about the gender of each royal family successors */
male(charles_prince).
male(andrew_prince).
male(edward_prince).
female(ann_princess).

/* relations between each successor to the monarch */
child(charles_prince,elizabeth_queen).
child(ann_princess,elizabeth_queen).
child(andrew_prince,elizabeth_queen).
child(edward_prince,elizabeth_queen).

/* age order of all the successors */
older(charles_prince,ann_princess).
older(ann_princess,andrew_prince).
older(andrew_prince,edward_prince).

/* age rules */
older_than(X,Y):-
	older(X,Y).

older_than(X,Y):-
	older(X,A),
	older(A,Y).

/* succession rules */
/* passed down the male line before female line */
succeed_before(X,Y):-
	male(X),
	female(Y).

/* passed down by age order in male line */
succeed_before(X,Y):-
	male(X),
	male(Y),
	older_than(X, Y).

/* passed down by age order in female line */
succeed_before(X,Y):-
	female(X),
	female(Y),
	older_than(X, Y).

/* sort succession list tail based on succession rules */
sort_successor_list(X,[Y|T],[Y|W]):- 
	\+(succeed_before(X,Y)), !, 
	sort_successor_list(X,T,W).

sort_successor_list(X,[Y|T],[X,Y|T]):-
	succeed_before(X,Y).

sort_successor_list(X,[],[X]).

/* generate succession line based on offspring list */
generate_succession_line([],[]).
generate_succession_line([X|Y],Succession_Line):-
	generate_succession_line(Y,List_Tail),
	sort_successor_list(X,List_Tail,Succession_Line).

/* main function to output succession line of queen elizabeth */
old_royal_succession(Succession_Line):- 
	findall(X,child(X,elizabeth_queen),Offspring), 
	generate_succession_line(Offspring,Succession_Line).
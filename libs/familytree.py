child(X,Y):-parent(Y,X)
spouse(X,Y):- child(P,X),child(P,Y)
husband(X,Y):-male(X),spouse(X,Y)
wife(X,Y):-female(X),spouse(X,Y)
son(X,Y):-male(X),child(X,Y)
    daughter(X,Y):-female(X),child(X,Y)
    mother(X,Y):-female(X),parent(X,Y)
    father(X,Y):-male(X),parent(X,Y)
    sibling(X,Y):-parent(P,X),parent(P,Y),X\=Y
    brother(X,Y):-male(X),sibling(X,Y)
    sister(X,Y):-female(X),sibling(X,Y)
    grandmother(X,Y):-mother(X,P),parent(P,Y)
    grandfather(X,Y):-father(X,P),parent(P,Y)
    grandson(X,Y):-son(X,P),parent(Y,P)
    granddaughter(X,Y):-daughter(X,P),parent(Y,P)
    aunt(X,Y):-sister(X,P),parent(P,Y)
    aunt(X,Y):-wife(X,P),sibling(P,Q),parent(Q,Y)
    uncle(X,Y):-brother(X,P),parent(P,Y)
    uncle(X,Y):-husband(X,P),sibling(P,Q),parent(Q,Y)
    niece(X,Y):-daughter(X,P),sibling(P,Y)
    niece(X,Y):-daughter(X,P),sibling(P,Q),spouse(Q,Y)
    nephew(X,Y):-son(X,P),sibling(P,Y)
    nephew(X,Y):-son(X,P),sibling(P,Q),spouse(Q,Y)
    cousin(X,Y):-parent(P,X),sibling(P,Q),spouse(Q,Y)
    cousin(X,Y):-parent(P,X),sibling(P,Q),parent(Q,Y)
    matGrandma(X,Y):-mother(X,P),mother(P,Y)
    putGrandma(X,Y):-mother(X,P),father(P,Y)
    matGrandpa(X,Y):-father(X,P),mother(P,Y)
    putGrandpa(X,Y):-father(X,P),father(P,Y)

male(John)
male(Brain)
male(Robert)
male(Hal)
male(Jeff)
male(Bobby)
male(Daniel)
male(Charles)
male(Frank)
male(Stanley)
male(Sean)
male(Zeke)
male(Steven)
male(George)

female(Jessica)
female(Lana)
female(Clara)
female(Lillie)
female(Ashely)
female(Tammy)
female(Lorrie)
female(Melissa)
female(Laura)
female(Lisa)
female(Annie)
female(Jillian)
female(Sally)
female(Pam)
female(Sabrina)
female(Marrie)
female(Doris)

parent(Daniel,John)
parent(Daniel,Brian)
parent(Daniel,Jessica)
parent(Charles,Hal)
parent(Frank,Robert)
parent(Frank,Lana)
parent(Frank,Clara)
parent(Frank,Lillie)
parent(Frank,Ashley)
parent(Stanley,Jeff)
parent(Stanley,Bobby)
parent(Stanley,Tammy)
parent(Stanley,Lorrie)
parent(Zeke,Melissa)
parent(Zeke,Laura)
parent(Steven,Daniel)
parent(Steven,Charles)
parent(Steven,Frank)
parent(George,Lisa)
parent(George,Stanley)
parent(George,Sean)
parent(George,Annie)

parent(Lisa,John)
parent(Lisa,Brian)
parent(Lisa,Jessica)
parent(Jillian,Hal)
parent(Sally,Robert)
parent(Sally,Lana)
parent(Sally,Clara)
parent(Sally,Lillie)
parent(Sally,Ashley)
parent(Pam,Jeff)
parent(Pam,Bobby)
parent(Pam,Tammy)
parent(Pam,Lorrie)
parent(Annie,Melissa)
parent(Annie,Laura)
parent(Annie,Daniel)
parent(Annie,Charles)
parent(Annie,Frank)
parent(Doris,Lisa)
parent(Doris,Stanley)
parent(Doris,Sean)
parent(Doris,Annie)



    
    
    
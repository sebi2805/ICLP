%
% Find the last element of a list.
%

-module(p01).
-export([last/1, myReverse/1, myReverseAux/2]).

last([Head | []]) -> 
    Head;

last([_ | Tail]) -> 
    last(Tail).

myReverseAux([], Acc) -> Acc;
myReverseAux([H | T], Acc) 
    -> myReverseAux(T, [H | Acc]).
myReverse(L) -> myReverseAux(L, []).
    
% To test:
% p01:last([1,2,3])
% p01:last([1])
%
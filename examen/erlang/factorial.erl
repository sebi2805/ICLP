-module(myfact).
-export([run/0]).

factorial(0) -> 1;
factorial(N) -> N * factorial(N - 1).

hello(S, X) -> 
    io:format("Hello ~s, factorialul este ~p!~n", [S, X]).

run() ->
    {ok, [Name]} = io:fread("Your Name: ", "~s"),
    {ok, [Val]} = io:fread("Your Number: ", "~d"),
    hello(Name, factorial(Val)).

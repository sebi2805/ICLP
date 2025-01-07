-module(main).
-export([start/0, loop/1]).


loop(N) ->
    if N > 10 -> io:format("Este mare~n");
        N < 10 -> io:format("Este mic~n")
    end.
start() ->
    loop(5),
    loop(12).

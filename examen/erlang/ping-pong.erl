-module(ppmod).
-export([start/0, pingN/2, pong/0]).

pingN(Pid, 0) ->
    Pid ! {self(), finished},
    io:format("Ping finished!~n");

pingN(Pid, N) ->
    Pid ! {self(), ping},
    receive
        {Pid, pong} ->
            io:format("Ping received Pong.~n")
    end,
    pingN(Pid, N - 1).

pong() ->
    receive
        {_Pid, finished} ->
            io:format("Game over.~n");
        {Pid, ping} ->
            io:format("Pong received Ping.~n"),
            Pid ! {self(), pong},
            pong()
    end.

start() ->
    PongId = spawn(ppmod, pong, []),
    spawn(ppmod, pingN, [PongId, 5]).

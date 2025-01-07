-module(example).

-export([start/0, loop/0]).

start() ->
    Pid = spawn(example, loop, []),
    Pid ! {self(), "Salut, proces!"},
    receive
        Reply -> io:format("Răspuns: ~p~n", [Reply])
    end.

loop() ->
    receive
        {Sender, Message} ->
            io:format("Primit: ~p~n", [Message]),
            Sender ! {ok, "Mesaj primit"}
    end.

-module(example).
-export([start_server/0, send_message/1]).

start_server() ->
    register(my_server, spawn(fun() -> server_loop() end)).

server_loop() ->
    receive
        {Msg, From} ->
            io:format("Received message: ~p~n", [Msg]),
            From ! {ok, Msg},
            server_loop();
        stop ->
            io:format("Stopping server~n"),
            ok
    end.

send_message(Msg) ->
    case whereis(my_server) of
        undefined ->
            io:format("Server is not running~n");
        Pid ->
            Pid ! {Msg, self()},
            receive
                {ok, Response} ->
                    io:format("Server responded: ~p~n", [Response])
            end
    end.

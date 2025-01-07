-module(main).
-export([start/0, server/1, filterClients/2, filterClients2/2, worker/3, calls/2, wait_worker/1]).

start() ->
    Server = spawn(main, server, [[]]),
    calls(Server, 100),
    Server ! {self(), get},
    receive 
        Clients -> io:format("~p~n", [Clients])
    end.



worker(Server, Parent, N) ->
    Server ! {self(), {add, N}}, 
    receive 
        Msg -> Parent ! Msg
    end.

calls(Server, N) ->
    Workers = [spawn(main, worker, [Server, self(), Value]) || Value <- lists:seq(0, N-1)],
    [wait_worker(W) || W <- Workers].
    
wait_worker(Worker) ->
    receive 
        {Worker, Msg} -> Msg
    end.

filterClients([], _) ->
    [];
filterClients([H | T], H) ->
    filterClients(T, H);
filterClients([H | T], C) ->
    [H | filterClients(T, C)].


filterClients2(List, Client) ->
    lists:filter(fun(C) -> C =/= Client end, List).

server(Clients) ->
    receive
        {From, {add, Client}} ->
            From ! {From, "Client was added"},
            server([Client | Clients]);
        {From, {remove, Client}} ->
            From ! "Client was removed",
            server(filterClients(Clients, Client));
        {From, get} ->
            From ! Clients,
            server(Clients)
    end.

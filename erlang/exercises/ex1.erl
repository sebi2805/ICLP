Exercițiul 1: Creează un server care gestionează o listă de utilizatori. Clientul poate trimite cereri pentru:

Adăugarea unui utilizator (add_user).
Ștergerea unui utilizator (remove_user).
Listarea tuturor utilizatorilor (list_users).
Serverul trebuie să trimită un răspuns înapoi fiecărui client cu starea actuală a listei după fiecare operație.

-module(main).
-export([start/0, server/1, filterClients/2, filterClients2/2]).

start() ->
    Server = spawn(main, server, [[]]),
    Server ! {self(), {add, "sebi"}},
    Server ! {self(), get},
    receive 
        Clients -> io:format("~p~n", [Clients])
    end,
    receive 
        Clients2 -> io:format("~p~n", [Clients2])
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
            From ! "Client was added",
            server([Client | Clients]);
        {From, {remove, Client}} ->
            From ! "Client was removed",
            server(filterClients(Clients, Client));
        {From, get} ->
            From ! Clients,
            server(Clients)
    end.

% mereu trb sa dai export la un modul si sa aiba acelasi nume ca fisierul
% Definirea modulului
-module(hello).

% Exportarea funcțiilor publice
-export([start/0]).

% Funcția principală
start() ->
    io:format("Salut, lume!~n").

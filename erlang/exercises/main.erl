-module(main).
-export([start/0, loop/1, find_length/1]).


start() ->
    Server = spawn(main, loop, [[]]),
    Server ! {self(), {enqueue, sebi}},
    receive
        {ok, Msg3} -> io:format("~p~n", [Msg3])
    end,
    Server ! {self(), peek},
    receive
        {error, Msg2} -> io:format("~p", [Msg2]);
        {ok, Msg1} -> io:format("~p", [Msg1])
    end
    .


loop(Elements) -> 
    receive
        {From, {enqueue, Item}} ->
            From ! {ok, "The item was added"}, 
            loop([Item | Elements]);
        {From, peek} -> 
            Length = find_length(Elements),
            if (Length > 0) -> 
                    [First | _] = Elements,
                    From ! {ok, First};
                true -> From ! {error, "Empty queue"}
            end
    end.


find_length([]) ->
    0;
find_length([_ | T]) ->
    Length = find_length(T),
    Length + 1.
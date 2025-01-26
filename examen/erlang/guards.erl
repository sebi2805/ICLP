prelg(X) when (X rem 2 == 0) ->
    io:format("Este par ~n");
prelg(_) ->
    io:format("Este impar ~n").


######################################

preli(X) ->
    Rez = if
        (X =< 1) and (X >= 0) -> "subunitar";
        (X > 1) -> "supraunitar";
        true -> "negativ"
    end,
    {X, Rez}.


######################################
prelc({S, X}) ->
    case {S, X} of
        {"pozitiv", X} when (X =< 1) and (X >= 0) -> "subunitar";
        {"pozitiv", X} when (X > 1) -> "supraunitar";
        {_, X} when (X >= 0) -> "pozitiv";
        _ -> "negativ"
    end.

start_server() -> 
    register(serv, spawn(fun() -> server_loop() end)).

server_loop() ->
    receive
        {From, {double, Number}} -> 
            From ! {serv, (Number * 2)},
            server_loop();
        {From, "Good Bye"} -> 
            From ! {serv, "Good Bye"},
            server_loop();
        {From, _} -> 
            From ! {serv, error},
            server_loop()
    end.

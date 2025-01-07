-module(sleep_example).
-compile(export_all).

sleep_demo() ->
    io:format("Start sleeping...~n"),
    timer:sleep(2000), % Timp în milisecunde (2 secunde)
    io:format("Finished sleeping!~n").

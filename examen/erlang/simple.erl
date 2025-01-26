prelA(X) when (X == 0) -> io:fwrite("End A ~n");
prelA(X) when (X > 0) -> io:fwrite("A ~n"), prelA(X - 1);
prelA(_) -> io:fwrite("Nothing ~n").
 
prelB(X) when (X == 0) -> io:fwrite("End B ~n");
prelB(X) when (X > 0) -> io:fwrite("B ~n"), prelB(X - 1);
prelB(_) -> io:fwrite("Nothing ~n").
 
myrec() ->
  receive
    { do_A, X } -> prelA(X), myrec();
    { do_B, X } -> prelB(X), myrec();
    _ -> io:format("Nothing ~n"), myrec()
  end.
 
start() ->
  Pid = spawn(fun() -> myrec() end),
  Pid ! { do_A, 3 },
  Pid ! { do_B, 2 },
  Pid ! { unknown, 1 },
  timer:sleep(3000).
 
main(_) -> start().
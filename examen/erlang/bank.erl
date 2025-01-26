
# Recap Erlang 

* variabile     Majuscula   + alfanum + @
                -

* atomi         minuscula
                literali

functional - numele functiilor sunt atomi
mai multe tipuri de egalitati dar cea care ne intereseaza este =:=
liste recursive     Prolog, haskell

                          [H | T]
(head-ul listei, 1 elemetn)     (tail-ul, o lista de elemente)


list = [1, X, [], f(Y), peter, john, ...]
[H|T] = [1, x, [], ...]

scrierea de head si tail -> head e primul element, tail e lista formata din restul elementelor

sum([]) -> 0;
sum([H|T]) -> H + sum(T).

operatorul , este conjunctia (daca vreau sa am mai multe instructiuni pun virgula intre)

# concurenta
    spawn(fun() -> ... end) 
    ia functia anonima si o executa in paralel pe un thread separat, si returneaza id-ul (Pid)
    toata concurenta se executa prin schimb de mesaje
.
    Pid ! msg. 
    transmit mesajul msg catre Pid
.
    mult din ce lucram trebuie tratat ca un automat de stari.
.
    1 ----msg----> 2
    |
    msg
    |
    2.
.
    receive
        msg1[when cond1] -> 
            exec 1;
        msg2 [where cond2] -> 
            exec2;
        - -> 
            exec3
    end
    
    Pid ! stop
     |
     v
     receive
     .
     .
     .
     stop -> 
        ...
    end.
.
    widthdraw(Amount)
    { widthdraw, Amount }
    act/0 msg transmis act  end.
    f(T1, T2, ... Tn) msg transmis {f, T1, T2, ... Tn}


    receive
        {widthdraw, From, Amount} when state =:= open


    cont bancar

    open <----close account ---------------activate account--------> closed
    (to itself:)
    widthdraw
    deposit
    check balance

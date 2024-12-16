import Control.Concurrent 
import Control.Monad 
import Data.List 
import Data.Maybe 
{- 

Problema. 

Un restaurant are N locuri. 
Initial, restaurantul este gol (toate locurile sunt marcate ca fiind libere). 
Cand un client soseste, se uita daca exista locuri libere si ocupa unul dintre ele pentru o anumita perioada de timp. 
Daca nu exista locuri libere, clientii sunt pusi intr-o coada de asteptare, iar apoi ocupa locurile care se elibereaza in ordinea sosirii. 

Creati un program care simuleaza functionarea restaurantului, avand cate un thread pentru fiecare client. 
Afisati mereu un mesaj cu locul pe care se asaza fiecare client, 
    afisati cand soseste, 
    afisati cand elibereaza locul,
    respectiv cand se asaza la coada.
-} 

data Loc = L | O deriving (Eq, Show) 
type MRestaurant = MVar ([Loc], [Int]) -- lista locurilor din restaurant 
                                       -- si coada  de asteptare

-- succes! 

liber :: Loc -> Bool 
liber loc = (loc == L) 

ocupat :: Loc -> Bool 
ocupat loc = (loc == O)

full :: [Loc] -> Bool 
full restaurant = and $ map ocupat restaurant 

ocupaloc i rest = let 
    (p1, p2) = splitAt i rest in p1 ++ (O : (tail p2)) 
    
-- [L, L, L, L, L]
-- [L, L] [L, L, L]
-- [L, L] ++ [O, L, L]
-- [L, L, O, L, L]

-- [1,2,3] = 1 : 2 : 3 : [] 
-- 1 : [2, 3, 4] = [1, 2, 3, 4]

-- [1,2] ++ [4, 5] = [1, 2, 3, 4]

elibloc i rest = let 
    (p1, p2) = splitAt i rest in p1 ++ (L : (tail p2))
    
takeprint :: MVar String -> IO () 
takeprint stdo = do 
    msg <- takeMVar stdo 
    putStrLn msg 
    
client restaurant stdo indexClient = do 
    (currentRestaurant, cq) <- takeMVar restaurant 
    if full currentRestaurant then do 
        putMVar restaurant (currentRestaurant, cq ++ [indexClient])
        putMVar stdo $ "Clientul " ++ show indexClient ++ " asteapta la coada"
    else do 
        let indexLoc = fromJust $ elemIndex L currentRestaurant
        let newRestaurant = ocupaloc indexLoc currentRestaurant 
        putMVar restaurant (newRestaurant, cq) 
        clientin restaurant stdo indexClient indexLoc 
        
clientin restaurant stdo indexClient indexLoc = do 
    putMVar stdo $ "Clientul " ++ show indexClient ++ " a ocupat locul " ++ show indexLoc 
    threadDelay 5000000
    putMVar stdo $ "Clientul " ++ show indexClient ++ " a parasit restaurantul"
    (currentRestaurant, cq) <- takeMVar restaurant 
    if null cq then 
        putMVar restaurant (elibloc indexLoc currentRestaurant, cq)
    else do 
        putMVar restaurant (currentRestaurant, tail cq) 
        clientin restaurant stdo (head cq) indexLoc 
        
main = do 
    stdo <- newEmptyMVar  
    restaurant <- newMVar ([L, L, L], []) 
    let clients = 5 
    mapM_ (forkIO . client restaurant stdo) [1..clients]
    
    forkIO $ forever $ takeprint stdo 
    
    getLine 
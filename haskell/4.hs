import Control.Concurrent 
import Control.Monad 

{- 
Reader-Writer 
- mai multe thread-uri au acces la o resursa 
- unele threaduri au rolul de Writer, altele rolul de Reader 
- resursa poate fi accesata simultan de mai multi cititori 
- dar poate fi accesata doar de un singur Writer la un moment de timp 

Implementam lock-uri folosind MVar-uri 

- un mutex care da acces la citit sau la scris, writeL 
- un monitor care sa inregistreze nr de cititori, readL 

-} 

type MyLock = MVar () 

newLock = newMVar () 
acquireLock m = takeMVar m 
releaseLock m = putMVar m () 

data MyRWLock = MyRWL { readL :: MVar Int, writeL :: MyLock } 

newMyRWLock :: IO MyRWLock
newMyRWLock = do 
    readL <- newMVar 0 
    writeL <- newLock 
    return (MyRWL readL writeL)
    
acquireWrite :: MyRWLock -> IO ()
acquireWrite (MyRWL readL writeL) = acquireLock writeL 

releaseWrite :: MyRWLock -> IO ()
releaseWrite (MyRWL readL writeL) = releaseLock writeL 

acquireRead :: MyRWLock -> IO ()
acquireRead (MyRWL readL writeL) = do 
    n <- takeMVar readL 
    if n == 0 then do 
        acquireLock writeL 
        putMVar readL 1 
    else 
        putMVar readL (n + 1) 

releaseRead :: MyRWLock -> IO ()
releaseRead (MyRWL readL writeL) = do 
    n <- takeMVar readL 
    if n == 1 then do 
        releaseLock writeL 
        putMVar readL 0 
    else 
        putMVar readL (n - 1) 
        
{- 
    mai departe se poate implementa Reader-Writer. 
-} 
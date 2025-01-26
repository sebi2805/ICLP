import java.io.File;
import java.io.FileWriter;
import java.io.Writer;
import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.ReentrantReadWriteLock;
import java.util.stream.Collectors;

class Drop {
    private ReentrantReadWriteLock lock = new ReentrantReadWriteLock();
    private LinkedList<String> messages = new LinkedList<>();

    public void write(String message) {
        lock.writeLock().lock();
        messages.add(message);
        lock.writeLock().unlock();
    }

    public String read(){
        lock.readLock().lock();
        var msg = messages.poll();
        lock.readLock().unlock();
        return msg;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Drop drop = new Drop();

        Thread t1 = new Thread(()->{
            while(true){
               drop.write(Thread.currentThread().getName() + new Random().nextInt());
                try {
                    Thread.sleep(new Random().nextInt(100, 300));
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
            }
        });

        Thread t2 = new Thread(()->{
            while(true){
                var msg = drop.read();
                System.out.println(msg);
                try {
                    Thread.sleep(new Random().nextInt(50, 150));
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
            }
        });

        Thread t3 = new Thread(()->{
            while(true){
                var msg = drop.read();
                System.out.println(msg);
                try {
                    Thread.sleep(new Random().nextInt(50, 150));
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
            }
        });

        t1.start();
        t2.start();
        t3.start();

        t1.join();
        t2.join();
        t3.join();
    }
}

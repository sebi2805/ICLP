import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingDeque;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

class Philosopher extends Thread {
    BlockingDeque<Philosopher> deque = new BlockingDeque<Philosopher>(10);
    private static int count = 0;
    private int index;
    private Philosopher left;
    private Philosopher right;
    private ReentrantLock lock = new ReentrantLock();
    public Condition notEating = lock.newCondition();
    public boolean isEating = false;
    public Philosopher() {
        count += 1;
        index = count;
    }
    public void setLeft(Philosopher left) {
        this.left = left;
    }
    public void setRight(Philosopher right) {
        this.right = right;
    }

    @Override
    public void run() {
        while (true) {
            lock.lock();
            while (left.isEating || right.isEating) {
                try {
                    left.notEating.await();
                    right.notEating.await();
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
            }
            isEating = true;
            System.out.println("Philosopher " + index + " is eating");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            isEating = false;
            notEating.signal();

            lock.unlock();
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            System.out.println("Philosopher " + index + " is thinking");

        }
    }
}
public class Main {
    public static void main(String[] args) throws Exception {
        List<Philosopher> philosophers = new ArrayList<Philosopher>();
        for (int i = 0; i < 5; i++) {
            philosophers.add(new Philosopher());
        }
        for (int i = 0; i < 5; i++) {
            philosophers.get(i).setLeft(philosophers.get(i-1 < 0 ? philosophers.size()-1 : i-1));
            philosophers.get(i).setRight(philosophers.get(i+1 > philosophers.size() - 1 ? 0 : i+1));
        }
        for (Philosopher p : philosophers) {
            p.start();
        }

        for (Philosopher p : philosophers) {
            p.join();
        }
    }
}

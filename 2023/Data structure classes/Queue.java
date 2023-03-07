import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.NoSuchElementException;

public class Queue implements Iterable<Integer> {
    private static int front, rear, capacity;
    private static int[] queue;

    public Queue(int capacitySize) {
        front = rear = 0;
        capacity = capacitySize;
        queue = new int[capacity];
    }

    public Queue() {
        front = rear = 0;
        capacity = 5;
        queue = new int[capacity];
    }

    public Object getFront() {
        if (front == rear) {
            return "Queue is empty!";
        }
        else {
            return (Integer)queue[front];
        }
    }

    public Object getRear() {
        if (front == rear) {
            return "Queue is empty!";
        }
        else {
            return (Integer)queue[rear];
        }
    }

    public int getFrontIndex() {
        return front;
    }

    public int getRearIndex() {
        return rear;
    }

    public int[] getQueue() {
        return queue;
    }

    public String toString() {
        String queueString = "FRONT - [";
        if (front == rear) {
            return queueString + "] - REAR";
        } else {
            for (int i=front; i<rear; i++) {
                if (i+1 == rear) {
                    queueString += Integer.toString(queue[i]) + "] - REAR";
                } else {
                    queueString += Integer.toString(queue[i]) + ", ";
                }
            }
        }
        return queueString;
    }

    public String printQueueArray() {
        String queueString = "[";
        for (int i=0;i<queue.length;i++) {
            if (i == queue.length-1) {
                queueString += Integer.toString(queue[i]) + "]";
            } else {
                queueString += Integer.toString(queue[i]) + ", ";
            }
        }
        return queueString;
    }

    public void resizeArray() {
        this.capacity *= 2;
        int[] temp = new int[capacity];
        for (int i=0; i<queue.length; i++) {
            temp[i] = queue[i];
        }
        this.queue = temp;
    }

    public void enqueue(int element) {
        if (capacity == rear) {
            resizeArray();
            queue[rear] = element;
            rear++;
        } else {
            queue[rear] = element;
            rear++;
        }
    }

    public Object dequeue() {
        if (front == rear) {
            System.out.println("Queue is empty");
            return null;
        } else {
            int element = queue[front];
            front++;
            return (Integer) element;
        }
    }

    public int size() {
        return rear - front;
    }

    @Override
    public Iterator<Integer> iterator() {
        return new MyIterator();
    }

    private class MyIterator implements Iterator<Integer> {
        private int frontTemp = front;

        @Override
        public boolean hasNext() {
            return frontTemp < rear;
        }

        @Override
        public Integer next() {
            if (hasNext()) {
                return queue[frontTemp++];
            } 
            throw new NoSuchElementException();
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException();
        }
    }
}

